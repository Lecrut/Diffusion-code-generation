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
def calculate_and_aggregate(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    aggregation = {}
    for condition, result in conditions:
        if result:
            aggregation[condition] = 1
        else:
            aggregation[condition] = 0
    return aggregation
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
        assert check_all_conditions(sample_conditions) == True
    def test_check_all_conditions_false(self):
        sample_conditions = [
            ("a", True),
            ("b", False)
        ]
        assert check_all_conditions(sample_conditions) == False
    def test_calculate_and_aggregate_mixed(self):
        sample_conditions = [
            ("A", True),
            ("B", False),
            ("C", True),
            ("D", False)
        ]
        expected = {
            "A": 1,
            "B": 0,
            "C": 1,
            "D": 0
        }
        actual = calculate_and_aggregate(sample_conditions)
        assert actual == expected
    def test_calculate_and_aggregate_all_true(self):
        sample_conditions = [
            ("X", True),
            ("Y", True)
        ]
        expected = {
            "X": 1,
            "Y": 1
        }
        actual = calculate_and_aggregate(sample_conditions)
        assert actual == expected
    def test_calculate_and_aggregate_all_false(self):
        sample_conditions = [
            ("P", False),
            ("Q", False)
        ]
        expected = {
            "P": 0,
            "Q": 0
        }
        actual = calculate_and_aggregate(sample_conditions)
        assert actual == expected
if __name__ == '__main__':
    analyzer = TestConditionAnalyzer()
    analyzer.test_analyze_conditions()
    analyzer.test_check_all_conditions_true()
    analyzer.test_check_all_conditions_false()
    analyzer.test_calculate_and_aggregate_mixed()
    analyzer.test_calculate_and_aggregate_all_true()
    analyzer.test_calculate_and_aggregate_all_false()
    print("All tests passed successfully.")