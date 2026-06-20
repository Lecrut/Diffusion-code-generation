class EqualityComparer:
    def compare(self, a, b):
        return a == b

if __name__ == '__main__':
    comparer = EqualityComparer()
    print(comparer.compare(5, 5))
    print(comparer.compare(10, 20))
    print(comparer.compare('hello', 'hello'))
    print(comparer.compare('hello', 'world'))