import random
from collections import Counter
from statistics import mean, median, stdev, variance
def generate_synthetic_data(seed=42):
    random.seed(seed)
    data_points = []
    for i in range(100):
        value = round(random.gauss(50.0, 10.0), 2)
        category = "A" if random.random() < 0.6 else ("B", "C")[random.randint(0, 1)]
        data_points.append({"id": i + 1, "value": value, "category": category})
    return data_points
def analyze_data(data):
    values = [item["value"] for item in data]
    categories = Counter([item["category"] for item in data])
    results = {
        "count": len(values),
        "mean": round(mean(values), 2),
        "median": median(values),
        "stdev": stdev(values) if values else None,
        "variance": variance(values) if values else None,
        "unique_categories": list(categories.keys()),
        "category_counts": dict(categories)
    }
    return results
if __name__ == '__main__':
    dataset = generate_synthetic_data()
    stats = analyze_data(dataset)
    print("Dataset Statistics:")
    for key, val in stats.items():
        if isinstance(val, list):
            print(f"{key}: {val}")
        else:
            print(f"{key}: {val}")