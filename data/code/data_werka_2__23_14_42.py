class ValueComparer:
    @staticmethod
    def compare(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparer = ValueComparer()
    result1 = comparer.compare(10, 5)
    print(result1)
    result2 = comparer.compare(7, 7)
    print(result2)
    result3 = comparer.compare(3, 9)
    print(result3)