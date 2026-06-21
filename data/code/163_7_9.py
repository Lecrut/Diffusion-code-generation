import csv

def serialize_to_csv(data):
    with open('fruits_colors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fruit', 'Color'])
        for fruit, color in data.items():
            writer.writerow([fruit, color])

if __name__ == '__main__':
    sample_data = {
        'Apple': 'Red',
        'Banana': 'Yellow',
        'Cherry': 'Red'
    }
    serialize_to_csv(sample_data)