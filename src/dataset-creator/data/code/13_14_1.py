from typing import List
def find_greatest_number(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return max(numbers)
class TestSuite:
    def run_tests(self):
        assert find_greatest_number([3, 7, 2, 9]) == 9
        assert find_greatest_number([-5, -2, -10, 4]) == 4
        assert find_greatest_number([42.5]) == 42.5
        assert find_greatest_number([8, 8, 8, 8]) == 8
        assert find_greatest_number([-100, -50, 0]) == 0
if __name__ == '__main__':
    test_runner = TestSuite()
    try:
        test_runner.run_tests()
        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"Test failed: {e}")