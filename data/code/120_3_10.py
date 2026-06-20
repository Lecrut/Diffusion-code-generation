class ValueComparer:
    @staticmethod
    def compare(val1, val2):
        return val1 == val2

if __name__ == '__main__':
    comparer = ValueComparer()
    print(comparer.compare(5, 5))
    print(comparer.compare(10, 5))
    print(comparer.compare("hello", "hello"))
    print(comparer.compare(3.14, 3.1400000000000004))