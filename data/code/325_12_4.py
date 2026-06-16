class QuantityComparator:
    def compare(self, quantity1, quantity2):
        if quantity1 > quantity2:
            return f"{quantity1} is greater than {quantity2}"
        elif quantity1 < quantity2:
            return f"{quantity2} is greater than {quantity1}"
        else:
            return f"{quantity1} is equal to {quantity2}"
if __name__ == '__main__':
    comparator = QuantityComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(3.14, 3.14))
    print(comparator.compare(200, 150))
    print(comparator.compare(7, 7))
    print(comparator.compare(-5, 10))
    print(comparator.compare(0, -1))