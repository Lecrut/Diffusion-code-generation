from typing import Any

class ValueChecker:
    def are_unequal(self, value1: Any, value2: Any) -> bool:
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_unequal(10, 20)
    print(result)