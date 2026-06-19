import csv

def calculate_average_weights(file_content):
    from collections import defaultdict

    reader = csv.DictReader(file_content.splitlines())
    category_weights = defaultdict(list)

    for row in reader:
        category = row['Category']
        weight = float(row['Weight'])
        category_weights[category].append(weight)

    average_weights = {category: sum(weights) / len(weights) for category, weights in category_weights.items()}
    return average_weights

if __name__ == '__main__':
    sample_csv_content = """Category,Weight
Fruits,1.2
Fruits,1.5
Vegetables,0.8
Vegetables,0.9
Dairy,1.0
Dairy,1.1"""

    average_weights = calculate_average_weights(sample_csv_content)
    print(average_weights)