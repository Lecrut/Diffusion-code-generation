class BitwiseBooleanChecker:
    def __init__(self, val_a: bool, val_b: bool) -> None:
        self.val_a = val_a
        self.val_b = val_b

    def check_both_false(self) -> bool:
        int_a = int(self.val_a)
        int_b = int(self.val_b)
        combined = int_a | int_b
        return not combined

def check_both_false(a: bool, b: bool) -> bool:
    checker = BitwiseBooleanChecker(a, b)
    return checker.check_both_false()

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    print(result1)
    result2 = check_both_false(True, False)
    print(result2)
    checker_instance = BitwiseBooleanChecker(False, True)
    result3 = checker_instance.check_both_false()
    print(result3)