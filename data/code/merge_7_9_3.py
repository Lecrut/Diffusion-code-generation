class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return NotImplemented
    def __repr__(self):
        return f"Pair({self.first}, {self.second})"
if __name__ == '__main__':
    pair1 = Pair(10, 20)
    pair2 = Pair(10, 20)
    pair3 = Pair(5, 15)
    print(f"Pair1: {pair1}")
    print(f"Pair2: {pair2}")
    print(f"Pair3: {pair3}")
    print(f"Are pair1 and pair2 equal? {pair1 == pair2}")
    print(f"Are pair1 and pair3 equal? {pair1 == pair3}")
    print(f"Are pair2 and pair3 equal? {pair2 == pair3}")