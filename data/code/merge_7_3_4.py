class ValueChecker:
    def check_equality(self, val1: object, val2: object) -> bool:
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"5 == 5: {checker.check_equality(5, 5)}")
    print(f"5 == 6: {checker.check_equality(5, 6)}")
    print(f"'hello' == 'hello': {checker.check_equality('hello', 'hello')}")
    print(f"'hello' == 'world': {checker.check_equality('hello', 'world')}")
    print(f"3.14 == 3.14: {checker.check_equality(3.14, 3.14)}")
    print(f"3.14 == 3.15: {checker.check_equality(3.14, 3.15)}")
    print(f"10 == '10': {checker.check_equality(10, '10')}")
    print(f"True == 1: {checker.check_equality(True, 1)}")