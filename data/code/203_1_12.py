class QuantityComparer:

    def __init__(self, quantity1: int, quantity2: int):
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def is_greater(self) -> bool:
        return self.quantity1 > self.quantity2
if __name__ == '__main__':
    comparer = QuantityComparer(50, 30)
    print(comparer.is_greater())