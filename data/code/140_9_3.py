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
    sample_conditions = [
        ("is_active", True),
        ("has_permission", False),
        ("is_admin", True)
    ]
    print("--- Analyzing Sample Conditions ---")
    print(f"Input Conditions: {sample_conditions}")
    analysis_result = analyze_and_summarize(sample_conditions)
    print("\nAnalysis Summary:")
    print(analysis_result)
    print("\n--- Testing Core Logic ---")
    test_set_1 = [("a", True), ("b", True)]
    print(f"Test Set 1 (All True): {check_all_true(test_set_1)}")
    test_set_2 = [("a", False), ("b", False)]
    print(f"Test Set 2 (All False): {check_all_false(test_set_2)}")
    test_set_3 = [("a", True), ("b", False)]
    print(f"Test Set 3 (Mixed): {check_all_true(test_set_3)}")
    print(f"Test Set 3 (Mixed): {check_all_false(test_set_3)}")