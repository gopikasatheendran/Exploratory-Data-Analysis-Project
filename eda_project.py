import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/gopik/Documents/eda/google-playstore-apps/Google-Playstore.csv')
print(df.head())
# Descriptive Statistics
print("Descriptive Statistics:")
print(df.describe())
# Check for Missing Data
print("\nMissing Data:")
print(df.isnull().sum())
# Visualize Missing Data
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Visualization")
plt.show()
missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)

# Plot the missing data percentage
plt.figure(figsize=(10, 6))
sns.barplot(x=missing_percentage.index, y=missing_percentage)
plt.xticks(rotation=90)
plt.ylabel('Percentage of Missing Values')
plt.title('Missing Values in Percentage')
plt.show()