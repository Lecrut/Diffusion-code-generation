import typing
def analyze_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    results = {}
    for condition, result in conditions:
        results[condition] = result
    return results
def check_all_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, result in conditions:
        if not result:
            return False
    return True
def aggregate_results(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    aggregated = {}
    for condition, result in conditions:
        if result:
            aggregated[condition] = "True"
        else:
            aggregated[condition] = "False"
    return aggregated
class TestConditionAnalyzer:
    def test_analyze_conditions(self):
        sample_conditions = [
            ("is_active", True),
            ("has_permission", False),
            ("is_admin", True)
        ]
        expected = {
            "is_active": True,
            "has_permission": False,
            "is_admin": True
        }
        actual = analyze_conditions(sample_conditions)
        assert actual == expected
    def test_check_all_conditions_true(self):
        sample_conditions = [
            ("a", True),
            ("b", True)
        ]
        assert check_all_conditions(sample_conditions) is True
    def test_check_all_conditions_false(self):
        sample_conditions = [
            ("a", True),
            ("b", False)
        ]
        assert check_all_conditions(sample_conditions) is False
    def test_aggregate_results(self):
        sample_conditions = [
            ("A", True),
            ("B", False),
            ("C", True)
        ]
        expected = {
            "A": "True",
            "B": "False",
            "C": "True"
        }
        actual = aggregate_results(sample_conditions)
        assert actual == expected
if __name__ == '__main__':
    analyzer = TestConditionAnalyzer()
    print("Running tests...")
    try:
        analyzer.test_analyze_conditions()
        print("test_analyze_conditions passed.")
        analyzer.test_check_all_conditions_true()
        print("test_check_all_conditions_true passed.")
        analyzer.test_check_all_conditions_false()
        print("test_check_all_conditions_false passed.")
        analyzer.test_aggregate_results()
        print("test_aggregate_results passed.")
        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"A test failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")