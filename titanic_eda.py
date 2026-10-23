import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)


# Inspect the dataset
print("Dataset Information:")
df.info()

print("\nDataset Statistics:")
print(df.describe())


# Handle missing values

# Fill missing ages with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing embarked values with the most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fill missing cabin values with "Unknown"
df["Cabin"] = df["Cabin"].fillna("Unknown")


# Remove duplicate rows
df = df.drop_duplicates()


# Filter first-class passengers
first_class = df[df["Pclass"] == 1]

print("\nFirst Class Passengers:")
print(first_class.head())


# Visualize survival rate by passenger class

# Calculate survival rate as a percentage
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

print("\nSurvival Rate by Passenger Class:")
for passenger_class, rate in survival_by_class.items():
    print(f"Class {passenger_class}: {rate:.2f}%")

survival_by_class.plot(kind="bar", color="skyblue")

plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate (%)")
plt.xlabel("Passenger Class")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_rate_by_class.png", dpi=300)
plt.show()


# Create a histogram of age distribution
sns.histplot(
    df["Age"],
    kde=True,
    bins=20,
    color="purple"
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("age_distribution.png", dpi=300)
plt.show()


# Create a scatter plot of age versus fare
plt.scatter(
    df["Age"],
    df["Fare"],
    alpha=0.5,
    color="green"
)

plt.title("Age versus Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("age_vs_fare.png", dpi=300)
plt.show()


# Save the cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as titanic_cleaned.csv")