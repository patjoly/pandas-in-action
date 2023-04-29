#!/usr/bin/env python
# coding: utf-8

# ## 7.1 The MultiIndex Object
import pandas as pd

address = ("8809 Flair Square", "Toddside", "IL", "37206")
address

addresses = [
    ("8809 Flair Square", "Toddside", "IL", "37206"),
    ("9901 Austin Street", "Toddside", "IL", "37206"),
    ("905 Hogan Quarter", "Franklin", "IL", "37206"),
]

# The two lines below are equivalent
pd.MultiIndex.from_tuples(addresses)
pd.MultiIndex.from_tuples(tuples = addresses)

row_index = pd.MultiIndex.from_tuples(
    tuples = addresses,
    names = ["Street", "City", "State", "Zip"]
)

row_index

data = [
    ["A", "B+"],
    ["C+", "C"],
    ["D-", "A"],
]

columns = ["Schools", "Cost of Living"]

area_grades = pd.DataFrame(
    data = data, index = row_index, columns = columns
)

area_grades

area_grades.columns

column_index = pd.MultiIndex.from_tuples([
    ("Culture", "Restaurants"),
    ("Culture", "Museums"),
    ("Services", "Police"),
    ("Services", "Schools"),
])

column_index

data = [
    ["C-", "B+", "B-", "A"],
    ["D+", "C", "A", "C+"],
    ["A-", "A", "D+", "F"], 
]

pd.DataFrame(
    data = data, index = row_index, columns = column_index
)

# ## 7.2 MultiIndex DataFrames
neighborhoods = pd.read_csv("neighborhoods.csv")
neighborhoods.head()

neighborhoods = pd.read_csv(
    "neighborhoods.csv",
    index_col = [0, 1, 2]
)

neighborhoods.head()

neighborhoods = pd.read_csv(
    "neighborhoods.csv",
    index_col = [0, 1, 2],
    header = [0, 1]
)

neighborhoods.head()

neighborhoods.info()

neighborhoods.index

neighborhoods.columns

neighborhoods.index.names

# The two lines below are equivalent
neighborhoods.index.get_level_values(1)
neighborhoods.index.get_level_values("City")

neighborhoods.columns.names

neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods.columns.names

neighborhoods.head(3)

# The two lines below are equivalent
neighborhoods.columns.get_level_values(0)
neighborhoods.columns.get_level_values("Category")

neighborhoods.head(1)

neighborhoods.nunique()

# ## 7.3 Sorting a MultiIndex
neighborhoods.sort_index()

neighborhoods.sort_index(ascending = False).head()

neighborhoods.sort_index(ascending = [True, False, True]).head()

# The two lines below are equivalent
neighborhoods.sort_index(level = 1)
neighborhoods.sort_index(level = "City")

# The two lines below are equivalent
neighborhoods.sort_index(level = [1, 2]).head()
neighborhoods.sort_index(level = ["City", "Street"]).head()

neighborhoods.sort_index(
    level = ["City", "Street"], ascending = [True, False]
).head()

# The two lines below are equivalent
neighborhoods.sort_index(axis = 1).head(3)
neighborhoods.sort_index(axis = "columns").head(3)

neighborhoods.sort_index(
    axis = 1, level = "Subcategory", ascending = False
).head(3)

neighborhoods = neighborhoods.sort_index(ascending = True)

neighborhoods.head(3)

# ## 7.4 Selecting with a MultiIndex
data = [
    [1, 2], 
    [3, 4]
]

df = pd.DataFrame(
    data = data,
    index = ["A", "B"],
    columns = ["X", "Y"]
)

df

df["X"]

# ### 7.4.1 Extracting One or More Columns
neighborhoods["Services"]
# **NOTE**: I've commented out the code below so that the Notebook can run without raising an error.
# neighborhoods["Schools"]

neighborhoods[("Services", "Schools")]

neighborhoods[[("Services", "Schools"), ("Culture", "Museums")]]

columns = [
    ("Services", "Schools"),
    ("Culture", "Museums")
]

neighborhoods[columns]

# ### 7.4.2 Extracting One or More Rows with loc
df

df.loc["A"]

df.iloc[1]

neighborhoods.loc[("TX", "Kingchester", "534 Gordon Falls")]

neighborhoods.loc["CA"]

neighborhoods.loc["CA", "Dustinmouth"]

neighborhoods.loc["CA", "Culture"]

neighborhoods.loc[("CA", "Dustinmouth")]

neighborhoods.loc[("CA", "Dustinmouth"), ("Services",)]

neighborhoods.loc[("CA", "Dustinmouth"), ("Services", "Schools")]

neighborhoods["NE":"NH"]

neighborhoods.loc[("NE", "Shawnchester"):("NH", "North Latoya")]

start = ("NE", "Shawnchester")
end   = ("NH", "North Latoya")
neighborhoods.loc[start:end]

neighborhoods.loc[("NE", "Shawnchester"):("NH")]

# ### 7.4.3 Extracting One or More Rows with iloc
neighborhoods.iloc[25]

neighborhoods.iloc[25, 2]

neighborhoods.iloc[[25, 30]]

neighborhoods.iloc[25:30]

neighborhoods.iloc[25:30, 1:3]

neighborhoods.iloc[-4:, -2:]

# ## 7.5 Cross Sections
# The two lines below are equivalent
neighborhoods.xs(key = "Lake Nicole", level = 1)
neighborhoods.xs(key = "Lake Nicole", level = "City")

neighborhoods.xs(
    axis = "columns", key = "Museums", level = "Subcategory"
).head()

# The two lines below are equivalent
neighborhoods.xs(
    key = ("AK", "238 Andrew Rue"), level = ["State", "Street"]
)

neighborhoods.xs(
    key = ("AK", "238 Andrew Rue"), level = [0, 2]
)

# ## 7.6. Manipulating the Index

# ### 7.6.1 Resetting the Index
neighborhoods.head()

new_order = ["City", "State", "Street"]
neighborhoods.reorder_levels(order = new_order).head()

neighborhoods.reorder_levels(order = [1, 0, 2]).head()

neighborhoods.reset_index().tail()

# The two lines below are equivalent
neighborhoods.reset_index(col_level = 1).tail()
neighborhoods.reset_index(col_level = "Subcategory").tail() 

neighborhoods.reset_index(
    col_fill = "Address", col_level = "Subcategory"
).tail()

neighborhoods.reset_index(level = "Street").tail()

neighborhoods.reset_index(level = ["Street", "City"]).tail()

neighborhoods.reset_index(level = "Street", drop = True).tail()

neighborhoods = neighborhoods.reset_index()

# ### 7.6.2 Setting the Index
neighborhoods.head(3)

neighborhoods.set_index(keys = "City").head()

neighborhoods.set_index(keys = ("Culture", "Museums")).head()

neighborhoods.set_index(keys = ["State", "City"]).head()

# ## 7.7 Coding Challenge

# ### 7.7.1 Problems
investments = pd.read_csv("investments.csv")
investments.head()

investments.nunique()

investments = investments.set_index(
    keys = ["Status", "Funding Rounds", "State"]
).sort_index()

investments.head()

# ### 7.7.2 Solutions
investments.loc[("Closed",)].head()

investments.loc[("Acquired", 10)]

investments.loc[("Operating", 6, "NJ")]

investments.loc[("Closed", 8), ("Name",)]

# The two lines below are equivalent
investments.xs(key = "NJ", level = 2).head()
investments.xs(key = "NJ", level = "State").head()

investments = investments.reset_index()
investments.head()

