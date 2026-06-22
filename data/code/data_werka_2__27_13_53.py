from typing import Any

class Comparator:
    @staticmethod
    def are_different(a: Any, b: Any) -> bool:
        return not Comparator.are_equal(a, b)

    @staticmethod
    def are_equal(a: Any, b: Any) -> bool:
        return a == b

if __name__ == '__main__':
    print(Comparator.are_different(1, 2))
    print(Comparator.are_different('a', 'b'))
    print(Comparator.are_different([1, 2], [1]))
    print(Comparator.are_different(3.0, 3))
    print(Comparator.are_different(None, None))

    sample1 = 42
    sample2 = "42"
    print(Comparator.are_different(sample1, sample2))

    value1 = 10
    value2 = "10"
    print(Comparator.are_different(value1, value2))
    value3 = [1, 2, 3]
    value4 = [1, 2, 3]
    print(Comparator.are_different(value3, value4))
    value5 = None
    value6 = None
    print(Comparator.are_different(value5, value6))
    value7 = 3.14
    value8 = 3.140000001
    print(Comparator.are_different(value7, value8))