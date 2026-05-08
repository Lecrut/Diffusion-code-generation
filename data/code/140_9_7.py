import typing
def analyze_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    results = {}
    for condition_name, condition_value in conditions:
        results[condition_name] = condition_value
    return results
def evaluate_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, bool]:
    evaluated_results = {}
    for condition_name, condition_value in conditions:
        evaluated_results[condition_name] = condition_value
    return evaluated_results
def check_all_true(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, condition_value in conditions:
        if not condition_value:
            return False
    return True
def check_any_true(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, condition_value in conditions:
        if condition_value:
            return True
    return False
def analyze_and_summarize(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    analysis = analyze_conditions(conditions)
    summary = {
        "all_true": check_all_true(conditions),
        "any_true": check_any_true(conditions),
        "raw_results": analysis
    }
    return summary
if __name__ == '__main__':
    sample_conditions = [
        ("is_active", True),
        ("has_permission", False),
        ("is_admin", True)
    ]
    print("--- Analyzing Conditions ---")
    raw_results = analyze_conditions(sample_conditions)
    print(f"Raw Results: {raw_results}")
    print("\n--- Evaluating Conditions ---")
    evaluated_results = evaluate_conditions(sample_conditions)
    print(f"Evaluated Results: {evaluated_results}")
    print("\n--- Summarizing Conditions ---")
    summary = analyze_and_summarize(sample_conditions)
    print(f"Summary: {summary}")
    print("\n--- Testing Specific Logic ---")
    print(f"Check All True: {check_all_true(sample_conditions)}")
    print(f"Check Any True: {check_any_true(sample_conditions)}")