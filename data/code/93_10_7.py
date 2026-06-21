class BooleanChecker:
    TRUE_CONST = True
    FALSE_CONST = False

    def are_both_false(self, first_val, second_val):
        is_first_false = first_val == self.FALSE_CONST
        is_second_false = second_val == self.FALSE_CONST
        return is_first_false and is_second_false

if __name__ == '__main__':
    checker = BooleanChecker()
    val_a = True
    val_b = False
    output = checker.are_both_false(val_a, val_b)
    print(output)