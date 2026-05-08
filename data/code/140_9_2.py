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
        ("A is positive", True),
        ("B is negative", False),
        ("C is zero", False),
        ("D is greater than 10", True)
    ]
    print("--- Analyzing Sample Conditions ---")
    analysis_result = analyze_and_summarize(sample_conditions)
    print(f"Analysis Result: {analysis_result}")
    print("\n--- Testing Core Functions ---")
    test_conditions_all_true = [
        ("X", True),
        ("Y", True)
    ]
    print(f"Check All True for {test_conditions_all_true}: {check_all_true(test_conditions_all_true)}")
    test_conditions_all_false = [
        ("P", False),
        ("Q", False)
    ]
    print(f"Check All False for {test_conditions_all_false}: {check_all_false(test_conditions_all_false)}")
    test_mixed_conditions = [
        ("M1", True),
        ("M2", False)
    ]
    print(f"Check All True for {test_mixed_conditions}: {check_all_true(test_mixed_conditions)}")
    print(f"Check All False for {test_mixed_conditions}: {check_all_false(test_mixed_conditions)}")