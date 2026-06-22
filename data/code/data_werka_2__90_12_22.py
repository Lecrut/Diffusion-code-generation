class BitwiseOrChecker:
    def __init__(self, val_a: bool, val_b: bool):
        self.val_a = val_a
        self.val_b = val_b

    def check_or_condition(self) -> bool:
        int_a = 1 if self.val_a else 0
        int_b = 1 if self.val_b else 0
        result_int = int_a | int_b
        return bool(result_int)

if __name__ == '__main__':
    checker = BitwiseOrChecker(True, False)
    result = checker.check_or_condition()
    print(result)
    
    checker2 = BitwiseOrChecker(False, False)
    result2 = checker2.check_or_condition()
    print(result2)