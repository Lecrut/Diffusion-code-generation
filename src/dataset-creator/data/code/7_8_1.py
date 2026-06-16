import unittest
class TrueFalseEvaluator:
    def evaluate(self, statement):
        return bool(statement) if isinstance(statement, str) else False
def run_tests():
    evaluator = TrueFalseEvaluator()
    test_cases = [
        ("The sky is blue", True),
        ("2 + 2 equals 5", False),
        (True, True),
        ([], False),
        ({}, False),
        ("10 > 9", True),
        ("False statement here", False),
    ]
    for input_val, expected in test_cases:
        result = evaluator.evaluate(input_val)
        assert result == expected, f"Failed for {input_val}: got {result}, expected {expected}"
if __name__ == '__main__':
    unittest.main()