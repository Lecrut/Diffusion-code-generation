class BooleanChecker:
    FALSE_VALUE = False

    def are_both_false(self, first, second):
        is_first_false = first == self.FALSE_VALUE
        is_second_false = second == self.FALSE_VALUE
        return is_first_false and is_second_false

if __name__ == '__main__':
    checker = BooleanChecker()
    val_a = False
    val_b = False
    outcome = checker.are_both_false(val_a, val_b)
    print(outcome)