from typing import Any

class InequalityChecker:
    @staticmethod
    def are_different(a: Any, b: Any) -> bool:
        return not a == b

if __name__ == '__main__':
    sample1 = 42
    sample2 = "42"
    print(InequalityChecker.are_different(sample1, sample2))

    value1 = 10
    value2 = "10"
    print(InequalityChecker.are_different(value1, value2))

    value3 = [1, 2, 3]
    value4 = [1, 2, 3]
    print(InequalityChecker.are_different(value3, value4))

    value5 = None
    value6 = None
    print(InequalityChecker.are_different(value5, value6))

    value7 = 3.14
    value8 = 3.140000001
    print(InequalityChecker.are_different(value7, value8))