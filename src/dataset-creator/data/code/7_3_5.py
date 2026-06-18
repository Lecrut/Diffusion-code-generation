class ValueChecker:
    def check_equality(self, val1: object, val2: object) -> bool:
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Checking (10, 10): {checker.check_equality(10, 10)}")
    print(f"Checking (10, 20): {checker.check_equality(10, 20)}")
    print(f"Checking (3.14, 3.14): {checker.check_equality(3.14, 3.14)}")
    print(f"Checking (3.14, 3.15): {checker.check_equality(3.14, 3.15)}")
    print(f"Checking ('hello', 'hello'): {checker.check_equality('hello', 'hello')}")
    print(f"Checking ('hello', 'world'): {checker.check_equality('hello', 'world')}")
    print(f"Checking (10, 10.0): {checker.check_equality(10, 10.0)}")