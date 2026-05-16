def categorize_conditions(conditions):
    categories = {
        "High_Priority": 0,
        "Medium_Priority": 1,
        "Low_Priority": 2
    }
    results = {}
    for condition in conditions:
        boolean_val, integer_val = condition
        priority = categories["Low_Priority"]
        if boolean_val and integer_val > 100:
            priority = categories["High_Priority"]
        elif boolean_val:
            priority = categories["Medium_Priority"]
        results[f"({boolean_val}, {integer_val})"] = priority
    return results
if __name__ == '__main__':
    sample_input = [
        (True, 50),
        (False, 150),
        (True, 10),
        (False, 200),
        (True, 101),
        (False, 5)
    ]
    categorized_data = categorize_conditions(sample_input)
    print(categorized_data)