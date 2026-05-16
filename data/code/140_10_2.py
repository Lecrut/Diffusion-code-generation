def categorize_conditions(conditions):
    categories = {
        "A": 0,
        "B": 0,
        "C": 0
    }
    for cond in conditions:
        if cond[0] and cond[1] == 10:
            categories["A"] += 1
        elif cond[0] and cond[1] < 10:
            categories["B"] += 1
        elif not cond[0] and cond[1] > 5:
            categories["C"] += 1
        else:
            categories["C"] += 1
    return categories
if __name__ == '__main__':
    input_data = [
        (True, 10),
        (True, 5),
        (False, 12),
        (False, 3),
        (True, 10),
        (False, 6)
    ]
    results = categorize_conditions(input_data)
    print(results)