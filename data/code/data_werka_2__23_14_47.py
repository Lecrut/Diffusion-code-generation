class ValueComparator:
    def compare(self, a, b):
        return (a > b) - (a < b)

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare(5, 3))
    print(comparator.compare(5, 5))
    print(comparator.compare(2, 8))