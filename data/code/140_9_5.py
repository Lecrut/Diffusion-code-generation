import typing
def analyze_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    results = {}
    for condition, result in conditions:
        results[condition] = result
    return results
def check_all_true(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, result in conditions:
        if not result:
            return False
    return True
def check_all_false(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, result in conditions:
        if result:
            return False
    return True
def analyze_and_summarize(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    analysis = analyze_conditions(conditions)
    summary = {
        "all_true": check_all_true(conditions),
        "all_false": check_all_false(conditions),
        "individual_results": analysis
    }
    return summary
if __name__ == '__main__':
    sample_conditions_1 = [
        ("A is positive", True),
        ("B is negative", False),
        ("C is zero", False)
    ]
    sample_conditions_2 = [
        ("X > 5", True),
        ("Y < 10", True),
        ("Z == 1", False)
    ]
    sample_conditions_3 = [
        ("P is true", True),
        ("Q is true", True)
    ]
    print("--- Analysis for Sample 1 ---")
    result1 = analyze_and_summarize(sample_conditions_1)
    print(result1)
    print("\n--- Analysis for Sample 2 ---")
    result2 = analyze_and_summarize(sample_conditions_2)
    print(result2)
    print("\n--- Analysis for Sample 3 ---")
    result3 = analyze_and_summarize(sample_conditions_3)
    print(result3)
    print("\n--- Testing check_all_true ---")
    print(f"Sample 1 all_true: {check_all_true(sample_conditions_1)}")
    print(f"Sample 2 all_true: {check_all_true(sample_conditions_2)}")
    print(f"Sample 3 all_true: {check_all_true(sample_conditions_3)}")
    print("\n--- Testing check_all_false ---")
    print(f"Sample 1 all_false: {check_all_false(sample_conditions_1)}")
    print(f"Sample 2 all_false: {check_all_false(sample_conditions_2)}")
    print(f"Sample 3 all_false: {check_all_false(sample_conditions_3)}")