import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "D:/DD/20jan/data.xlsx"  
data = pd.read_excel(file_path)
# descriptive statistics
print(data.describe())

numeric_cols = data.select_dtypes(include='number')


# CO2 Emissions Over the Years
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='co2', data=data, marker='o', linestyle='-', color='r')
plt.title('CO2 Emissions Over the Years')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (million metric tons)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# CO2 Emissions per Capita vs. GDP with Regression Line
plt.figure(figsize=(10, 6))
sns.regplot(x='gdp', y='co2_per_capita', data=data, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('CO2 Emissions per Capita vs. GDP with Regression Line')
plt.xlabel('GDP (trillion USD)')
plt.ylabel('CO2 Emissions per Capita (metric tons)')
plt.show()

# Box Plot of Energy Consumption per Capita
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['energy_per_capita'])
plt.title('Box Plot of Energy Consumption per Capita')
plt.xlabel('Energy Consumption per Capita')
plt.show()

# Total CO2 Emissions by Year

plt.figure(figsize=(12, 6))
sns.barplot(x='year', y='co2', data=data, ci=None, color='green')  
plt.title('Total CO2 Emissions by Year')
plt.xlabel('Year')
plt.ylabel('Total CO2 Emissions (million metric tons)')
plt.show()

# Cumulative CO2 Emissions Over the Years
plt.figure(figsize=(12, 6))
data_cumulative = data[['year', 'cumulative_co2']]
data_cumulative = data_cumulative.groupby('year').sum().reset_index()
plt.fill_between(data_cumulative['year'], data_cumulative['cumulative_co2'], color='orange', alpha=0.4)
plt.plot(data_cumulative['year'], data_cumulative['cumulative_co2'], label='Cumulative CO2 Emissions', color='blue')
plt.title('Cumulative CO2 Emissions Over the Years')
plt.xlabel('Year')
plt.ylabel('Cumulative CO2 Emissions (million metric tons)')
plt.legend()
plt.show()
# Correlation
additional_vars = ['consumption_co2', 'coal_co2', 'gas_co2', 'oil_co2']
additional_correlation_matrix = data[additional_vars].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(additional_correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation  ')
plt.show()


data['year'] = pd.to_datetime(data['year'], format='%Y')

# Time Series Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='co2', data=data, marker='o',color='blue')
plt.title('Time Series of CO2 Emissions Over the Years')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (million metric tons)')
plt.show()
