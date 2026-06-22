class BooleanChecker:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def check_both_false(self) -> bool:
        return not (self.a | self.b)

def check_both_false(a: bool, b: bool) -> bool:
    checker = BooleanChecker(a, b)
    return checker.check_both_false()

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = check_both_false(val_a, val_b)
    print(result)
    checker_instance = BooleanChecker(False, True)
    print(checker_instance.check_both_false())