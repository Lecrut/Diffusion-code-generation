def categorize_conditions(conditions):
    categories = {
        "high_priority": 0,
        "medium_priority": 1,
        "low_priority": 2
    }
    results = []
    for cond in conditions:
        boolean_val = cond[0]
        integer_val = cond[1]
        category = "low_priority"
        if boolean_val and integer_val > 100:
            category = "high_priority"
        elif boolean_val or integer_val > 50:
            category = "medium_priority"
        results.append({
            "input": cond,
            "category": category
        })
    return results
if __name__ == '__main__':
    sample_conditions = [
        (True, 150),
        (False, 50),
        (True, 10),
        (False, 200),
        (True, 45),
        (False, 101)
    ]
    categorized_data = categorize_conditions(sample_conditions)
    for item in categorized_data:
        print(f"Input: {item['input']}, Category: {item['category']}")