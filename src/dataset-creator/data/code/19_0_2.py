import random
from datetime import datetime, timedelta
from collections import defaultdict
import statistics
def generate_synthetic_data(num_records=100):
    data = []
    base_date = datetime.now() - timedelta(days=num_records)
    for i in range(num_records):
        timestamp = (base_date + timedelta(minutes=i)).isoformat()
        value_a = sum(random.random() for _ in range(12)) / 6 - 0.5
        categories = ['A', 'B', 'C']
        category = random.choice(categories)
        data.append({
            "id": i,
            "timestamp": timestamp,
            "value_a": round(value_a, 4),
            "category": category
        })
    return data
def analyze_data(data):
    values = [row["value_a"] for row in data]
    categories_counts = defaultdict(int)
    for item in data:
        categories_counts[item["category"]] += 1
    mean_val = statistics.mean(values) if values else None
    median_val = statistics.median(values) if len(values) > 0 else None
    std_dev = statistics.stdev(values) if len(values) > 1 else None
    return {
        "mean": round(mean_val, 4),
        "median": round(median_val, 4),
        "std_deviation": round(std_dev, 4),
        "category_distribution": dict(categories_counts),
        "total_records": len(data)
    }
if __name__ == '__main__':
    raw_data = generate_synthetic_data()
    stats_result = analyze_data(raw_data)
    print(f"Total Records: {stats_result['total_records']}")
    print(f"Mean Value: {stats_result['mean']}")
    print(f"Median Value: {stats_result['median']}")
    print(f"Standard Deviation: {stats_result['std_deviation']}")
    for cat, count in stats_result["category_distribution"].items():
        percentage = (count / len(raw_data)) * 100
        print(f"{cat}: {percentage:.2f}% ({count} occurrences)")