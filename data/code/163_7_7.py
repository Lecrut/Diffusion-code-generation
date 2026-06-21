import csv

def serialize_fruit_colors(fruits, colors):
    with open('fruit_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for fruit, color in zip(fruits, colors):
            writer.writerow([fruit, color])

if __name__ == '__main__':
    fruits_list = ["orange", "grape", "kiwi", "mango"]
    colors_list = ["orange", "purple", "green", "yellow"]
    serialize_fruit_colors(fruits_list, colors_list)