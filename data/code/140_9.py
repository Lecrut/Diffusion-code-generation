import typing
def analyze_condition(condition: typing.Union[bool, typing.List[bool]]) -> typing.Dict[str, typing.Any]:
    results = {}
    if isinstance(condition, bool):
        results['is_true'] = condition
        results['is_false'] = not condition
        results['original_value'] = condition
    elif isinstance(condition, list):
        results['is_list'] = True
        results['total_elements'] = len(condition)
        results['true_count'] = sum(condition)
        results['false_count'] = len(condition) - sum(condition)
        results['all_true'] = all(condition)
        results['all_false'] = all(not b for b in condition)
        results['contains_true'] = any(condition)
    else:
        results['error'] = 'Invalid input type provided.'
    return results
def test_analyze_condition():
    test_cases = [
        (True, "Single True"),
        (False, "Single False"),
        ([True, True, False], "List with mixed values"),
        ([True, True, True], "List with all True"),
        ([False, False, False], "List with all False"),
        ([], "Empty List"),
        ([True], "List with one True"),
        ([False], "List with one False"),
    ]
    for input_val, description in test_cases:
        print(f"--- Testing: {description} ---")
        result = analyze_condition(input_val)
        print(f"Input: {input_val}")
        print(f"Result: {result}")
        if description == "Single True":
            assert result['is_true'] is True and result['is_false'] is False
        elif description == "Single False":
            assert result['is_true'] is False and result['is_false'] is True
        elif description == "List with mixed values":
            assert result['is_list'] is True
            assert result['true_count'] == 2
            assert result['false_count'] == 1
            assert result['all_true'] is False
            assert result['contains_true'] is True
        elif description == "List with all True":
            assert result['true_count'] == 3
            assert result['all_true'] is True
            assert result['contains_true'] is True
        elif description == "List with all False":
            assert result['true_count'] == 0
            assert result['all_false'] is True
            assert result['contains_true'] is False
        elif description == "Empty List":
            assert result['is_list'] is True
            assert result['total_elements'] == 0
            assert result['true_count'] == 0
            assert result['all_true'] is True
            assert result['all_false'] is True
            assert result['contains_true'] is False
        elif description == "List with one True":
            assert result['true_count'] == 1
            assert result['contains_true'] is True
        elif description == "List with one False":
            assert result['true_count'] == 0
            assert result['contains_true'] is False
        else:
            pass
    print("\nAll core logic tests completed successfully (based on hard-coded checks).")
if __name__ == '__main__':
    test_analyze_condition()