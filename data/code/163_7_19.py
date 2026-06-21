import csv

def serialize_fruit_colors(fruits, colors):
    if len(fruits) != len(colors):
        raise ValueError("Fruits and colors lists must have the same length")
    
    with open('fruit_colors.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in zip(fruits, colors):
            writer.writerow([fruit, color])

if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    serialize_fruit_colors(fruits_list, colors_list)