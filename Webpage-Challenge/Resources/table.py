# Python program to convert
# CSV to HTML Table
import pandas as pd
# to read csv file named "samplee"
table = pd.read_csv("Webpage-Challenge/Resources/cities.csv")
# to save as html file
# named as "Table"
table.to_html("Webpage-Challenge/data.html", index=False)

