def categorize_conditions(conditions):
    categories = {
        "TypeA": 0,
        "TypeB": 1,
        "TypeC": 2
    }
    results = {}
    for i, (bool_val, int_val) in enumerate(conditions):
        if bool_val and int_val > 10:
            results[f"TypeA"] = results.get(f"TypeA", 0) + 1
        elif not bool_val and int_val < 0:
            results[f"TypeB"] = results.get(f"TypeB", 0) + 1
        else:
            results[f"TypeC"] = results.get(f"TypeC", 0) + 1
    return results
def process_data(input_conditions):
    return categorize_conditions(input_conditions)
if __name__ == '__main__':
    sample_conditions = [
        (True, 15),
        (False, -5),
        (True, 5),
        (False, 10),
        (True, 20),
        (False, 0)
    ]
    categorized_data = process_data(sample_conditions)
    print(categorized_data)