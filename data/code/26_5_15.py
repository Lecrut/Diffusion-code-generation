class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        """Returns True if self.value > other.value, False otherwise."""
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    checker_a = NumberChecker(10)
    checker_b = NumberChecker(5)

    result_1 = checker_a.is_greater_than(checker_b)  # Should be True (10 > 5)
    print(f"{checker_a.value} is greater than {checker_b.value}: {result_1}")

    checker_c = NumberChecker(3)
    result_2 = checker_a.is_greater_than(checker_c)  # Should be True (10 > 3)
    print(f"{checker_a.value} is greater than {checker_c.value}: {result_2}")

    result_3 = checker_b.is_greater_than(checker_a)  # Should be False (5 <= 10)
    print(f"{checker_b.value} is greater than {checker_a.value}: {result_3}")