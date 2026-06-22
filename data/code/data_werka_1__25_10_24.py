from typing import Union

class ValueChecker:

    def check_for_zero(self, value: Union[int, float]) -> bool:
        return value == 0
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check_for_zero(0))
    print(checker.check_for_zero(10))
    print(checker.check_for_zero(-0.0))
    print(checker.check_for_zero(3.14))