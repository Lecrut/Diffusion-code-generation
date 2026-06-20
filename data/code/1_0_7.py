import csv
import io

def calculate_category_averages(csv_content):
    reader = csv.DictReader(io.StringIO(csv_content))
    category_totals = {}
    category_counts = {}
    
    for row in reader:
        if 'category' not in row or 'weight' not in row:
            continue
        category = row['category']
        try:
            weight = float(row['weight'])
        except ValueError:
            continue
        
        if category not in category_totals:
            category_totals[category] = 0.0
            category_counts[category] = 0
        
        category_totals[category] += weight
        category_counts[category] += 1
    
    averages = {}
    for category in category_totals:
        if category_counts[category] > 0:
            averages[category] = category_totals[category] / category_counts[category]
        else:
            averages[category] = 0.0
    
    return averages

if __name__ == '__main__':
    sample_csv = """id,category,weight
1,apples,150
2,bananas,120
3,apples,180
4,oranges,200
5,bananas,130
6,oranges,210"""
    
    result = calculate_category_averages(sample_csv)
    print(result)