class FastComparer:
    @staticmethod
    def compare(a, b):
        return a == b

if __name__ == '__main__':
    comparer = FastComparer()
    print(comparer.compare(10, 10))
    print(comparer.compare('hello', 'hello'))
    print(comparer.compare([1, 2], [1, 2]))
    print(comparer.compare({'a': 1}, {'a': 1}))
    print(comparer.compare(None, None))
    print(comparer.compare(10, '10'))