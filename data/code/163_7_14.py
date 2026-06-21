import csv

def serialize_fruit_colors(fruits, colors):
    with open('fruit_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in zip(fruits, colors):
            writer.writerow([fruit, color])

if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Cherry']
    colors = ['Red', 'Yellow', 'Red']
    serialize_fruit_colors(fruits, colors)