class QuantityComparer:
    def __init__(self, quantity1, quantity2):
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def exceeds(self):
        return self.quantity1 > self.quantity2

if __name__ == '__main__':
    comparer1 = QuantityComparer(5, 3)
    print(f"Does 5 exceed 3? {comparer1.exceeds()}")

    comparer2 = QuantityComparer(2, 4)
    print(f"Does 2 exceed 4? {comparer2.exceeds()}")