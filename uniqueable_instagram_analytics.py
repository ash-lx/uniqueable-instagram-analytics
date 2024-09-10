# Instagram Analytics Data
data = [
    {
        "S.no": 1,
        "Post type": "one product",
        "Age Range": "25-45",
        "Female": 100.0,
        "Male": 0.00,
        "Location": "Germany",
        "Accounts Reached": 283,
        "Profile Visit": 7,
        "Spent": 2.60,
        "Cost per profile visit": 0.37
    },
    {
        "S.no": 2,
        "Post type": "one product",
        "Age Range": "25-45",
        "Female": 100.0,
        "Male": 0.00,
        "Location": "Berlin, Hamburg, Frankfurt, Munich",
        "Accounts Reached": 268,
        "Profile Visit": 5,
        "Spent": 2.93,
        "Cost per profile visit": 0.59
    },
    {
        "S.no": 3,
        "Post type": "one product",
        "Age Range": "25-45",
        "Female": 100.0,
        "Male": 0.00,
        "Location": "Leipzig",
        "Accounts Reached": 396,
        "Profile Visit": 4,
        "Spent": 2.76,
        "Cost per profile visit": 0.69
    },
    {
        "S.no": 4,
        "Post type": "multiple products",
        "Age Range": "25-45",
        "Female": 75.0,
        "Male": 25.00,
        "Location": "Germany",
        "Accounts Reached": 224,
        "Profile Visit": 2,
        "Spent": 3.02,
        "Cost per profile visit": 1.51
    },
    {
        "S.no": 5,
        "Post type": "reel",
        "Age Range": "25-45",
        "Female": 75.0,
        "Male": 25.00,
        "Location": "Germany",
        "Accounts Reached": 318,
        "Profile Visit": 8,
        "Spent": 2.80,
        "Cost per profile visit": 0.35
    },
    {
        "S.no": 6,
        "Post type": "first customer",
        "Age Range": "18+",
        "Female": 85.0,
        "Male": 15.00,
        "Location": "Germany",
        "Accounts Reached": 201,
        "Profile Visit": 9,
        "Spent": 3.06,
        "Cost per profile visit": 0.34
    },
    {
        "S.no": 7,
        "Post type": "product",
        "Age Range": "18+",
        "Female": 75.0,
        "Male": 25.00,
        "Location": "France + Germany",
        "Accounts Reached": 1290,
        "Profile Visit": 34,
        "Spent": 10.00,
        "Cost per profile visit": 0.29
    }
]

df = pd.DataFrame(data)

# Set the style for all plots
sns.set_theme(style="whitegrid")  # Use seaborn's set_theme instead of plt.style.use

# 1. Overall Campaign Efficiency Overview
plt.figure(figsize=(12, 6))
bars = plt.bar(df['S.no'], df['Cost per profile visit'], color=plt.cm.viridis(np.linspace(0, 1, len(df))))
plt.title('Cost per Profile Visit by Campaign', fontsize=16)
plt.xlabel('Campaign Number', fontsize=12)
plt.ylabel('Cost per Profile Visit (€)', fontsize=12)
plt.xticks(df['S.no'])

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'€{height:.2f}',
             ha='center', va='bottom')

plt.show()

# 2. Demographic Targeting Efficiency
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Female', y='Male', size='Profile Visit', hue='Cost per profile visit', data=df, sizes=(50, 500), palette='coolwarm')
plt.title('Gender Targeting vs. Efficiency')
plt.xlabel('Female Audience (%)')
plt.ylabel('Male Audience (%)')
plt.show()

# 3. Geographic Efficiency Comparison (Expanded)
plt.figure(figsize=(15, 10))

# Create a subplot for Cost per Profile Visit
plt.subplot(2, 1, 1)
sns.barplot(x='Location', y='Cost per profile visit', data=df, palette='Set2')
plt.title('Cost per Profile Visit by Location', fontsize=16)
plt.xlabel('Location', fontsize=12)
plt.ylabel('Cost per Profile Visit (€)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of each bar
for i, v in enumerate(df['Cost per profile visit']):
    plt.text(i, v, f'€{v:.2f}', ha='center', va='bottom')

# Create a subplot for Profile Visits
plt.subplot(2, 1, 2)
sns.barplot(x='Location', y='Profile Visit', data=df, palette='Set2')
plt.title('Profile Visits by Location', fontsize=16)
plt.xlabel('Location', fontsize=12)
plt.ylabel('Number of Profile Visits', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of each bar
for i, v in enumerate(df['Profile Visit']):
    plt.text(i, v, str(v), ha='center', va='bottom')

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Additional insight: Efficiency vs. Reach scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['Accounts Reached'], df['Cost per profile visit'],
                      c=df['Spent'], s=df['Profile Visit']*20,
                      cmap='viridis', alpha=0.7)

plt.title('Efficiency vs. Reach by Location', fontsize=16)
plt.xlabel('Accounts Reached', fontsize=12)
plt.ylabel('Cost per Profile Visit (€)', fontsize=12)

# Add location labels to each point
for i, location in enumerate(df['Location']):
    plt.annotate(location, (df['Accounts Reached'][i], df['Cost per profile visit'][i]),
                 xytext=(5, 5), textcoords='offset points')

# Add colorbar to show spending
cbar = plt.colorbar(scatter)
cbar.set_label('Total Spent (€)', fontsize=10)

# Add legend for bubble size
sizes = [20, 100, 500]
labels = ['Small', 'Medium', 'Large']
legend_elements = [plt.scatter([], [], s=size, c='gray', alpha=0.7, label=label)
                   for size, label in zip(sizes, labels)]
plt.legend(handles=legend_elements, title='Profile Visits', loc='upper left')

plt.tight_layout()
plt.show()

# 4. Post Type Efficiency
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Post type', y='Cost per profile visit', size='Profile Visit', hue='Spent', data=df, sizes=(50, 500), palette='viridis')
plt.title('Post Type Efficiency')
plt.xlabel('Post Type')
plt.ylabel('Cost per Profile Visit (€)')
plt.xticks(rotation=45, ha='right')
plt.show()

# 5. Spend vs. Efficiency Analysis
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Spent', y='Cost per profile visit', size='Profile Visit', hue='Post type', data=df, sizes=(50, 500))
plt.title('Ad Spend vs. Cost Efficiency')
plt.xlabel('Total Spent (€)')
plt.ylabel('Cost per Profile Visit (€)')
plt.show()

# 6. Profile Visits vs. Efficiency
plt.figure(figsize=(12, 6))
sns.regplot(x='Profile Visit', y='Cost per profile visit', data=df, scatter_kws={'s': 100})
plt.title('Relationship between Profile Visits and Cost per Visit')
plt.xlabel('Profile Visits')
plt.ylabel('Cost per Profile Visit (€)')
plt.show()