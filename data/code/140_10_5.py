def categorize_conditions(conditions):
    categories = {
        "high_priority": 0,
        "medium_priority": 1,
        "low_priority": 2
    }
    results = {}
    for i, (is_active, threshold) in enumerate(conditions):
        priority = categories["low_priority"]
        if is_active and threshold > 100:
            priority = categories["high_priority"]
        elif is_active and threshold > 50:
            priority = categories["medium_priority"]
        results[f"condition_{i}"] = {
            "active": is_active,
            "threshold": threshold,
            "priority": priority
        }
    return results
if __name__ == '__main__':
    sample_conditions = [
        (True, 150),
        (False, 75),
        (True, 40),
        (False, 200),
        (True, 51)
    ]
    categorized_data = categorize_conditions(sample_conditions)
    for key, data in categorized_data.items():
        print(f"{key}: Active={data['active']}, Threshold={data['threshold']}, Priority={data['priority']}")