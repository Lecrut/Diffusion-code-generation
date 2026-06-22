import csv
import os
import tempfile

def calculate_average_weights(csv_path: str) -> dict:
    category_sums = {}
    category_counts = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['category'].strip()
            try:
                weight = float(row['weight'].strip())
            except (ValueError, KeyError):
                continue
            if category in category_sums:
                category_sums[category] += weight
                category_counts[category] += 1
            else:
                category_sums[category] = weight
                category_counts[category] = 1
    averages = {}
    for category in category_sums:
        if category_counts[category] > 0:
            averages[category] = category_sums[category] / category_counts[category]
    return averages

def create_sample_csv() -> str:
    fd, path = tempfile.mkstemp(suffix='.csv', text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write('category,weight\n')
            f.write('Apple,150.5\n')
            f.write('Apple,160.0\n')
            f.write('Apple,145.5\n')
            f.write('Banana,120.0\n')
            f.write('Banana,130.0\n')
            f.write('Orange,200.0\n')
    except Exception:
        os.close(fd)
        raise
    return path
if __name__ == '__main__':
    sample_csv_path = create_sample_csv()
    try:
        result = calculate_average_weights(sample_csv_path)
        print(result)
    finally:
        os.unlink(sample_csv_path)