class QuantityComparator:
    def __init__(self, quantity1: int, quantity2: int):
        if not isinstance(quantity1, int) or not isinstance(quantity2, int):
            raise ValueError("Both arguments must be integers.")
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def is_first_greater(self) -> bool:
        return self.quantity1 > self.quantity2

if __name__ == '__main__':
    comparator = QuantityComparator(50, 30)
    print(comparator.is_first_greater())