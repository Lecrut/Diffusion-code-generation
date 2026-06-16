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
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 15))
    print(comparator.compare(100, 99))
    print(comparator.compare(42, 42))