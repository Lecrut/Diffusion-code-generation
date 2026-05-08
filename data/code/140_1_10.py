def analyze_conditions(conditions):
    if not conditions:
        return True
    and_results = []
    or_results = []
    for condition, result in conditions.items():
        if result:
            and_results.append(True)
            or_results.append(True)
        else:
            and_results.append(False)
            or_results.append(False)
    and_result = all(and_results)
    if not or_results:
        return and_result
    else:
        or_result = any(or_results)
        return and_result or or_result
if __name__ == '__main__':
    sample_conditions_1 = {
        "A": True,
        "B": False,
        "C": True
    }
    print(f"Sample 1 Result: {analyze_conditions(sample_conditions_1)}")
    sample_conditions_2 = {
        "X": True,
        "Y": True,
        "Z": True
    }
    print(f"Sample 2 Result: {analyze_conditions(sample_conditions_2)}")
    sample_conditions_3 = {
        "P": False,
        "Q": False
    }
    print(f"Sample 3 Result: {analyze_conditions(sample_conditions_3)}")
    sample_conditions_4 = {}
    print(f"Sample 4 Result: {analyze_conditions(sample_conditions_4)}")
    sample_conditions_5 = {
        "M": False,
        "N": True
    }
    print(f"Sample 5 Result: {analyze_conditions(sample_conditions_5)}")