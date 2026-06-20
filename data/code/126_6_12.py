class Comparator:
    def compare(self, x, y):
        return x == y

if __name__ == '__main__':
    comparator = Comparator()
    result1 = comparator.compare(5, 5)
    print(f"Checking equality between 5 and 5: {result1}")
    result2 = comparator.compare(10, 20)
    print(f"Checking equality between 10 and 20: {result2}")
    result3 = comparator.compare(3.14, 3.14)
    print(f"Checking equality between 3.14 and 3.14: {result3}")