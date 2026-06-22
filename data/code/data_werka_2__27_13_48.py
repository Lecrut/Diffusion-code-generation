from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

class DifferenceChecker:
    def __init__(self, value1: Any, value2: Any):
        self.value1 = value1
        self.value2 = value2

    def check_difference(self) -> bool:
        return are_different(self.value1, self.value2)

if __name__ == '__main__':
    checker1 = DifferenceChecker(5, 10)
    print(checker1.check_difference())

    checker2 = DifferenceChecker('hello', 'world')
    print(checker2.check_difference())

    checker3 = DifferenceChecker([1, 2], [3, 4])
    print(checker3.check_difference())

    checker4 = DifferenceChecker(7.5, 7.5)
    print(checker4.check_difference())

    checker5 = DifferenceChecker(True, False)
    print(checker5.check_difference())