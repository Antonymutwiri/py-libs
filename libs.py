# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. NumPy - Create array and calculate mean
print("=== NumPy Task ===")
numbers = np.arange(1, 11)  # Array of numbers 1-10
mean = np.mean(numbers)
print(f"Numbers: {numbers}")
print(f"Mean: {mean}\n")

# 2. Pandas - Load dataset and show statistics
print("=== Pandas Task ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 28, 35],
    'Salary': [50000, 65000, 58000, 72000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\n")

# 3. Requests - Fetch from public API
print("=== Requests Task ===")
try:
    response = requests.get('https://api.github.com/users/octocat')
    if response.status_code == 200:
        user_data = response.json()
        print(f"GitHub user 'octocat' has {user_data['public_repos']} public repositories")
    else:
        print(f"API request failed with status code {response.status_code}")
except Exception as e:
    print(f"Error fetching API data: {e}")
print("\n")

# 4. Matplotlib - Create line plot
print("=== Matplotlib Task ===")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()