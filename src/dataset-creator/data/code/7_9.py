class ValuePair:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def are_equal(self):
        return self.value1 == self.value2
if __name__ == '__main__':
    pair1 = ValuePair(10, 10)
    pair2 = ValuePair(5, 5)
    pair3 = ValuePair(10, 11)
    print(f"Pair 1 equality check: {pair1.are_equal()}")
    print(f"Pair 2 equality check: {pair2.are_equal()}")
    print(f"Pair 3 equality check: {pair3.are_equal()}")