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
    a1, b1 = 10, 5
    result1 = comparator.compare(a1, b1)
    print(f"Comparing {a1} and {b1}: {result1}")
    a2, b2 = 7, 7
    result2 = comparator.compare(a2, b2)
    print(f"Comparing {a2} and {b2}: {result2}")
    a3, b3 = 20, 15
    result3 = comparator.compare(a3, b3)
    print(f"Comparing {a3} and {b3}: {result3}")