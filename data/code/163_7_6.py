import csv

def serialize_fruit_colors():
    data = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Cherry", "Red"),
        ("Date", "Brown"),
        ("Elderberry", "Purple")
    ]
    
    with open('fruits_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fruit", "Color"])
        for fruit, color in data:
            writer.writerow([fruit, color])

if __name__ == '__main__':
    serialize_fruit_colors()