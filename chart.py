import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#generate synthetic customer spending data for boxplot
data = {
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Spending': [200, 150, 300, 250, 400]
}
df = pd.DataFrame(data)
# Create a boxplot using seaborn to be saved as 512x512 pixel image
plt.figure(figsize=(5.12, 5.12), dpi=100)
sns.boxplot(x='Customer', y='Spending', data=df)
plt.title('Customer Spending Distribution')
plt.xlabel('Customer')
plt.ylabel('Spending ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart.png', dpi=100)
plt.close()
