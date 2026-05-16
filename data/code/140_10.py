def categorize_conditions(conditions):
    categories = {
        "high_priority": 0,
        "medium_priority": 1,
        "low_priority": 2
    }
    results = {}
    for condition in conditions:
        boolean_val, integer_val = condition
        category_score = 0
        if boolean_val and integer_val > 100:
            category_score = categories["high_priority"]
        elif boolean_val or integer_val > 50:
            category_score = categories["medium_priority"]
        else:
            category_score = categories["low_priority"]
        results[f"({boolean_val}, {integer_val})"] = category_score
    return results
if __name__ == '__main__':
    sample_input = [
        (True, 150),
        (False, 20),
        (True, 45),
        (False, 101),
        (True, 10),
        (False, 55)
    ]
    categorized_data = categorize_conditions(sample_input)
    for key, value in categorized_data.items():
        print(f"{key}: {value}")