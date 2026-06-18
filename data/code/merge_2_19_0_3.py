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
        flag = True if random.random() < 0.7 else False
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
    for record in data:
        categories[record["category"]].append(record["value"])
    results = {}
    for cat_name, values in categories.items():
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values) if len(values) > 0 else 0
        flag_count = sum(1 for r in data if r["category"] == cat_name and r["flag"])
        results[cat_name] = {
            "count": len(values),
            "mean": round(mean_val, 2),
            "variance": round(variance, 4),
            "positive_flags": flag_count / len(data) if data else 0.0
        }
    return results
if __name__ == '__main__':
    raw_data = generate_synthetic_data()
    stats = analyze_data(raw_data)
    print(stats)