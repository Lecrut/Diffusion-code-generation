import csv

def serialize_fruit_colors(fruit_color_pairs):
    with open('fruit_colors.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in fruit_color_pairs:
            writer.writerow([fruit, color])

if __name__ == '__main__':
    sample_pairs = [
        ('Apple', 'Red'),
        ('Banana', 'Yellow'),
        ('Cherry', 'Red')
    ]
    serialize_fruit_colors(sample_pairs)