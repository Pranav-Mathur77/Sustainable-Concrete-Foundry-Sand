import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/compressive_strength.csv")

print("Dataset:")
print(df)

# Convert data for plotting
pivot_df = df.pivot(index="Days", columns="Mix", values="Strength_MPa")

# Plot graph
pivot_df.plot(marker='o')

plt.title("Compressive Strength vs Days")
plt.xlabel("Curing Days")
plt.ylabel("Strength (MPa)")

plt.grid()

plt.show()
