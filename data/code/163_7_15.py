import csv

def serialize_fruit_colors():
    fruit_color_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("grape", "purple")
    ]
    
    with open('fruits_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in fruit_color_pairs:
            writer.writerow([fruit, color])

if __name__ == '__main__':
    serialize_fruit_colors()