import random
from datetime import datetime, timedelta
from collections import defaultdict
def generate_synthetic_data(num_records=100):
    data = []
    base_date = datetime.now() - timedelta(days=365)
    for i in range(num_records):
        timestamp = (base_date + timedelta(days=random.randint(0, 364))).isoformat()
        category = random.choice(['A', 'B', 'C'])
        value = round(random.gauss(100, 25), 2)
        flag = random.random() > 0.7
        data.append({
            "id": i + 1,
            "timestamp": timestamp,
            "category": category,
            "value": value,
            "flag": flag
        })
    return data
def analyze_data(data):
    categories = defaultdict(list)
    for item in data:
        categories[item["category"]].append(item["value"])
    stats = {}
    for cat_name, values in categories.items():
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values) if len(values) > 0 else 0
        stats[cat_name] = {
            "count": len(values),
            "mean": round(mean_val, 4),
            "variance": round(variance, 4)
        }
    return data, stats
if __name__ == '__main__':
    raw_data = generate_synthetic_data(100)
    processed_data, analysis_results = analyze_data(raw_data)
    print(f"Total records: {len(processed_data)}")
    for cat_name in sorted(analysis_results.keys()):
        info = analysis_results[cat_name]
        print(f"{cat_name}: Count={info['count']}, Mean={info['mean']}, Variance={info['variance']}")