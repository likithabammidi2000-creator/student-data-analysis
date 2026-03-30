import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["A","B","C","D"],
    "Marks": [85,90,78,92]
}

df = pd.DataFrame(data)

print(df)

sns.barplot(x=df["Name"], y=df["Marks"])
plt.title("Student Marks Analysis")
plt.show()
