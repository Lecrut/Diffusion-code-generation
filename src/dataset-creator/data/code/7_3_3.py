class ValueChecker:
    def check_equality(self, val1: object, val2: object) -> bool:
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Checking 10 and 10: {checker.check_equality(10, 10)}")
    print(f"Checking 'hello' and 'hello': {checker.check_equality('hello', 'hello')}")
    print(f"Checking 5 and 6: {checker.check_equality(5, 6)}")
    print(f"Checking True and True: {checker.check_equality(True, True)}")
    print(f"Checking 3.14 and 3.1400000000000001: {checker.check_equality(3.14, 3.1400000000000001)}")