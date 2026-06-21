import csv

def serialize_fruit_colors(fruits, colors):
    with open('fruit_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in zip(fruits, colors):
            writer.writerow([fruit, color])

if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    serialize_fruit_colors(fruits_list, colors_list)
    print("Fruit and color pairs have been serialized to fruit_colors.csv")