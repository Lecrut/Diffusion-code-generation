from typing import Any

class Comparator:
    @staticmethod
    def are_different(a: Any, b: Any) -> bool:
        return a != b

if __name__ == '__main__':
    sample1 = 10
    sample2 = "10"
    print(Comparator.are_different(sample1, sample2))

    sample3 = [1, 2, 3]
    sample4 = [1, 2, 3]
    print(Comparator.are_different(sample3, sample4))

    sample5 = None
    sample6 = None
    print(Comparator.are_different(sample5, sample6))

    sample7 = 3.14
    sample8 = 3.140000001
    print(Comparator.are_different(sample7, sample8))