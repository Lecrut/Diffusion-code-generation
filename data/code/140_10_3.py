def categorize_conditions(conditions):
    categories = {
        "A": 0,
        "B": 0,
        "C": 0
    }
    for cond in conditions:
        if cond[0] is True and cond[1] > 10:
            categories["A"] += 1
        elif cond[0] is False and cond[1] < 5:
            categories["B"] += 1
        else:
            categories["C"] += 1
    return categories
if __name__ == '__main__':
    sample_conditions = [
        (True, 15),
        (False, 3),
        (True, 20),
        (False, 1),
        (True, 8),
        (False, 6)
    ]
    result = categorize_conditions(sample_conditions)
    print(result)