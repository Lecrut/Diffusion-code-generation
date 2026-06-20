class QuantityComparator:
    def __init__(self, quantity1: int, quantity2: int):
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def exceeds(self) -> bool:
        return self.quantity1 > self.quantity2

if __name__ == '__main__':
    comparator1 = QuantityComparator(50, 30)
    print(f"Does 50 exceed 30? {comparator1.exceeds()}")

    comparator2 = QuantityComparator(25, 75)
    print(f"Does 25 exceed 75? {comparator2.exceeds()}")