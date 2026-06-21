import csv

def serialize_fruit_colors():
    fruit_colors = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Cherry", "Red"),
        ("Grape", "Purple"),
        ("Kiwi", "Green")
    ]
    
    with open('fruit_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fruit", "Color"])
        for fruit, color in fruit_colors:
            writer.writerow([fruit, color])

if __name__ == '__main__':
    serialize_fruit_colors()