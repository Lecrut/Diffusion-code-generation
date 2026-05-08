def categorize_conditions(conditions):
    categories = {
        "high_priority": 0,
        "medium_priority": 1,
        "low_priority": 2
    }
    results = {}
    for i, (is_active, threshold) in enumerate(conditions):
        category = "low_priority"
        if is_active and threshold > 100:
            category = "high_priority"
        elif is_active and threshold > 50:
            category = "medium_priority"
        results[f"condition_{i}"] = category
    return results
if __name__ == '__main__':
    sample_input = [
        (True, 150),
        (False, 200),
        (True, 45),
        (False, 90),
        (True, 101)
    ]
    categorized_data = categorize_conditions(sample_input)
    print(categorized_data)