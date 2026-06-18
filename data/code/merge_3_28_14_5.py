import random

class NumberSorter:
    """A class designed to handle numerical sorting logic."""

    def __init__(self, value):
        self._value = value

    @property
    def value(self) -> int | float:
        return self._value

    def is_greater_than(self, other_value: int | float) -> bool:
        """Checks if the object's internal value is larger than the provided other_value.

        Args:
            other_value (int | float): The value to compare against.

        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self._value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    samples = [42, 100.5, -7]

    sorter_1 = NumberSorter(8)
    print(f"Testing value: {sorter_1.value}")

    test_cases = [3, 9, 10]

    for tc in test_cases:
        result = sorter_1.is_greater_than(tc)
        print(f"is_greater_than({tc}): {result}")

    # Demonstrate with a random value generated locally (no network/files)
    random_value = random.randint(-50, 50)
    another_sorter = NumberSorter(random_value * 2)
    print(f"\nRandom test: Comparing {random_value} and {another_sorter.value}")
    result_random = sorter_1.is_greater_than(another_sorter.value)
    print(f"Is 8 > {another_sorter.value}? {result_random}")

    # Verify the property access works as expected
    assert isinstance(sorter_1, NumberSorter)
    assert sorter_1.value == 8
    
    final_check = sorter_1.is_greater_than(90)
    print(f"\nFinal check: is 8 > 90? {final_check}") # Should be False

    if not final_check and random_value * 2 < 8:
        extra_tester = NumberSorter(random_value * 2 + 10)
        assert sorter_1.is_greater_than(extra_tester.value), "Assertion failed for logic verification"