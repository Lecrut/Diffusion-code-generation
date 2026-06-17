class QuantityComparator:
    def compare(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
if __name__ == '__main__':
    comparator = QuantityComparator()
    result1 = comparator.compare(10, 5)
    print(f"Comparing 10 and 5: {result1}")
    result2 = comparator.compare(3, 7)
    print(f"Comparing 3 and 7: {result2}")
    result3 = comparator.compare(42, 42)
    print(f"Comparing 42 and 42: {result3}")