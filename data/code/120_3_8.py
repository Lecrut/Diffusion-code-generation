class ValueComparator:
    def compare(self, value1, value2):
        return value1 == value2

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare(5, 5))
    print(comparator.compare(10, 5))
    print(comparator.compare("hello", "hello"))
    print(comparator.compare(3.14, 3.1400000000000004))