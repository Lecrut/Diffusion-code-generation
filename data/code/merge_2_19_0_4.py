import random
from datetime import datetime, timedelta
from collections import defaultdict
def generate_synthetic_data(num_records=100):
    data = []
    base_date = datetime.now() - timedelta(days=num_records)
    for i in range(num_records):
        timestamp = (base_date + timedelta(days=i)).isoformat()
        value_a = round(random.uniform(0, 100), 2)
        value_b = round(value_a * random.random(), 2)
        data.append({
            "id": i + 1,
            "timestamp": timestamp,
            "value_a": value_a,
            "value_b": value_b
        })
    return data
def calculate_statistics(data):
    values = [row["value_a"] for row in data]
    count = len(values)
    total = sum(values)
    mean_val = total / count if count > 0 else 0
    variance_sum = sum((x - mean_val) ** 2 for x in values)
    variance = variance_sum / (count - 1) if count > 1 else 0
    std_dev = round(variance ** 0.5, 4)
    min_val = min(values)
    max_val = max(values)
    return {
        "sample_size": count,
        "mean": round(mean_val, 2),
        "standard_deviation": std_dev,
        "min_value": min_val,
        "max_value": max_val
    }
def main():
    raw_data = generate_synthetic_data(100)
    stats_result = calculate_statistics(raw_data)
    print(f"Sample Size: {stats_result['sample_size']}")
    print(f"Mean Value: {stats_result['mean']}")
    print(f"Standard Deviation: {stats_result['standard_deviation']}")
    print(f"Min Value: {stats_result['min_value']}")
    print(f"Max Value: {stats_result['max_value']}")
if __name__ == '__main__':
    main()