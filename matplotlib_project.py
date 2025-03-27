
import matplotlib.pyplot as plt
import numpy as np

# Create simple data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Sine Wave')
plt.title('Simple Sine Wave Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('simple_plot.png')
plt.show()

# Create a simple bar chart
plt.figure(figsize=(8, 6))
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]
plt.bar(categories, values)
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Save the plot
plt.savefig('bar_chart.png')
plt.show() 