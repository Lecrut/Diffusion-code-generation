class FastComparator:
    def compare(self, a, b):
        return a == b

if __name__ == '__main__':
    comparator = FastComparator()
    print(comparator.compare(10, 10))
    print(comparator.compare('hello', 'hello'))
    print(comparator.compare([1, 2], [1, 2]))
    print(comparator.compare({'a': 1}, {'a': 1}))
    print(comparator.compare(None, None))
    print(comparator.compare(10, '10'))