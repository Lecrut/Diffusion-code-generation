import random
from datetime import datetime, timedelta
from collections import defaultdict
def generate_synthetic_data(num_records=100):
    data = []
    base_date = datetime.now() - timedelta(days=num_records)
    for i in range(num_records):
        timestamp = (base_date + timedelta(days=i)).isoformat()
        value_a = round(random.uniform(0, 100), 2)
        value_b = round(value_a * random.uniform(0.5, 1.5), 2)
        data.append({
            'id': i + 1,
            'timestamp': timestamp,
            'value_a': value_a,
            'value_b': value_b
        })
    return data
def calculate_statistics(data):
    values = [row['value_a'] for row in data]
    sum_val = sum(values)
    mean_val = sum_val / len(values) if values else 0
    variance_sum = sum((x - mean_val) ** 2 for x in values)
    variance = variance_sum / len(values) if values else 0
    std_dev = variance ** 0.5
    min_val = min(values)
    max_val = max(values)
    return {
        'count': len(data),
        'sum': round(sum_val, 2),
        'mean': round(mean_val, 4),
        'variance': round(variance, 4),
        'std_deviation': round(std_dev, 4),
        'min_value': min_val,
        'max_value': max_val
    }
def main():
    raw_data = generate_synthetic_data()
    stats_result = calculate_statistics(raw_data)
    print(f"Total Records: {stats_result['count']}")
    print(f"Sum of Value A: {stats_result['sum']}")
    print(f"Mean of Value A: {stats_result['mean']}")
    print(f"Variance: {stats_result['variance']}")
    print(f"Standard Deviation: {stats_result['std_deviation']}")
    print(f"Minimum Value: {stats_result['min_value']}")
    print(f"Maximum Value: {stats_result['max_value']}")
if __name__ == '__main__':
    main()