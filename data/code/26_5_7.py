class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        """Returns True if this instance's value is greater than another instance's value."""
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    checker_a = NumberChecker(10)
    checker_b = NumberChecker(5)

    result_1 = checker_a.is_greater_than(checker_b)
    
    checker_c = NumberChecker(3)
    result_2 = checker_b.is_greater_than(checker_c)

    print(f"{checker_a.value} > {checker_b.value}: {result_1}")
    print(f"{checker_b.value} > {checker_c.value}: {result_2}")