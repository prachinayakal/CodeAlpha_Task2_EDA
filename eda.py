import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("books_scraped_all.csv")

# Clean & preprocess
df['Price'] = df['Price'].replace('£', '', regex=True).astype(float)
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].map(rating_map)
  
# Check structure
print("📄 Dataset Head:")
print(df.head())
print("\n📝 Data Types:")
print(df.dtypes)
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Describe data
print("\n📊 Summary Statistics:")
print(df.describe())

# Plot: Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title("Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.show()

# Plot: Rating Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Rating', data=df)
plt.title("Book Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Plot: Availability
plt.figure(figsize=(6,4))
sns.countplot(x='Availability', data=df)
plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Hypothesis Test: Are higher-rated books more expensive?
plt.figure(figsize=(8,6))
sns.boxplot(x='Rating', y='Price', data=df)
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.show()

avg_price_by_rating = df.groupby('Rating')['Price'].mean()
print("\n💰 Average Price by Rating:")
print(avg_price_by_rating)

# Availability counts
avail_counts = df['Availability'].value_counts()
print("\n📦 Availability Counts:")
print(avail_counts)
