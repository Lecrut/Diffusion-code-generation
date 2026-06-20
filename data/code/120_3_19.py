class ValueComparer:
    def compare(self, x, y):
        return x == y

if __name__ == '__main__':
    comparer = ValueComparer()
    print(comparer.compare(5, 5))
    print(comparer.compare("hello", "hello"))
    print(comparer.compare(3.14, 3.1400000000000004))
    print(comparer.compare(10, 20))