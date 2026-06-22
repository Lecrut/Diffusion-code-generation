class NumericComparer:
    def compare(self, a: int, b: int) -> int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparer = NumericComparer()
    result1 = comparer.compare(5, 3)
    print(result1)
    result2 = comparer.compare(10, 10)
    print(result2)
    result3 = comparer.compare(1, 2)
    print(result3)