class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __eq__(self, other):
        if not isinstance(other, Pair):
            return NotImplemented
        return self.first == other.first and self.second == other.second
    def equals(self, other):
        if not isinstance(other, Pair):
            return False
        return self.first == other.first and self.second == other.second
if __name__ == '__main__':
    pair1 = Pair(10, 20)
    pair2 = Pair(10, 20)
    pair3 = Pair(5, 15)
    print(f"Pair 1: ({pair1.first}, {pair1.second})")
    print(f"Pair 2: ({pair2.first}, {pair2.second})")
    print(f"Pair 3: ({pair3.first}, {pair3.second})")
    result1 = pair1.equals(pair2)
    print(f"Is Pair 1 equal to Pair 2? {result1}")
    result2 = pair1.equals(pair3)
    print(f"Is Pair 1 equal to Pair 3? {result2}")
    result3 = pair1 == pair2
    print(f"Is Pair 1 == Pair 2 (using __eq__)? {result3}")