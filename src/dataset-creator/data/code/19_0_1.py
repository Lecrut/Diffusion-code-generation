import random
from datetime import datetime, timedelta
from collections import defaultdict
def generate_synthetic_data(num_records=100):
    data = []
    base_date = datetime.now() - timedelta(days=num_records)
    for i in range(num_records):
        timestamp = (base_date + timedelta(minutes=i)).isoformat()
        value_a = round(random.uniform(5, 25), 4)
        value_b = round(value_a * random.uniform(0.8, 1.2), 4)
        data.append({
            "id": i + 1,
            "timestamp": timestamp,
            "value_a": value_a,
            "value_b": value_b,
            "category": ["Alpha", "Beta"][i % 2]
        })
    return data
def perform_statistical_analysis(data):
    values = [row["value_a"] for row in data]
    categories = defaultdict(list)
    for item in data:
        cat_name = item["category"]
        val_b = item["value_b"]
        categories[cat_name].append(val_b)
    stats = {
        "mean_value_a": sum(values) / len(values),
        "std_deviation": (sum((x - sum(values)/len(values))**2 for x in values) / len(values)) ** 0.5,
        "min_value_a": min(values),
        "max_value_a": max(values),
    }
    category_stats = {}
    for cat_name, vals in categories.items():
        mean_cat = sum(vals) / len(vals)
        std_cat = (sum((x - mean_cat)**2 for x in vals) / len(vals)) ** 0.5
        category_stats[cat_name] = {"mean": round(mean_cat, 4), "std_deviation": round(std_cat, 4)}
    return stats, category_stats
if __name__ == '__main__':
    raw_data = generate_synthetic_data(120)
    global_stats, cat_stats = perform_statistical_analysis(raw_data)
    print(f"Global Mean: {global_stats['mean_value_a']:.4f}")
    print(f"Global Std Dev: {global_stats['std_deviation']:.4f}")
    for cat_name in ["Alpha", "Beta"]:
        if cat_name in cat_stats:
            s = cat_stats[cat_name]
            print(f"{cat_name} Mean: {s['mean']}")