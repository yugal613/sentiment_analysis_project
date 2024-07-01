import matplotlib.pyplot as plt

# Sample data
categories = ['Happiness and Pride',
              "Inspiration and Motivation",
              "Nostalgia and Sentimentality",
              "Empathy and Understanding",
              "Responsibility and Commitment",
              "Uncertainty and Fear",
              "Gratitude and Appreciation",
              "Compassion and Support",
              "Ambition and Vision"]

values = [5, 7, 3, 8, 4,6,2,1,6]

# Create a bar graph
plt.bar(categories, values)

# Add titles and labels
plt.title('Sample Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Show the plot
plt.show()
