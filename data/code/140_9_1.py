import typing
def analyze_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    results = {}
    for condition_str, condition_bool in conditions:
        results[condition_str] = condition_bool
    return results
def check_all_conditions(conditions: typing.List[typing.Tuple[str, bool]]) -> bool:
    for _, condition_bool in conditions:
        if not condition_bool:
            return False
    return True
def analyze_and_verify(conditions: typing.List[typing.Tuple[str, bool]]) -> typing.Dict[str, typing.Any]:
    analysis = analyze_conditions(conditions)
    verification_result = check_all_conditions(conditions)
    analysis['all_true'] = verification_result
    return analysis
class TestAnalyzer:
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
    def test_analyze_and_verify_mixed(self):
        sample_conditions = [
            ("A", True),
            ("B", False),
            ("C", True)
        ]
        expected = {
            "A": True,
            "B": False,
            "C": True,
            "all_true": False
        }
        actual = analyze_and_verify(sample_conditions)
        assert actual == expected
if __name__ == '__main__':
    analyzer = TestAnalyzer()
    analyzer.test_analyze_conditions()
    analyzer.test_check_all_conditions_true()
    analyzer.test_check_all_conditions_false()
    analyzer.test_analyze_and_verify_mixed()