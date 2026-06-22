from typing import Any

class ValueChecker:
    def are_equal(self, a: Any, b: Any) -> bool:
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_equal(10, 10)
    print(result)