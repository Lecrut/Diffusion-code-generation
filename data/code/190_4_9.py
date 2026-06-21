class TupleChecker:
    def __init__(self, data):
        self.data = data

    def check_existence(self, target):
        return target in self.data

if __name__ == '__main__':
    checker1 = TupleChecker((1, 2, 3, 4, 5))
    print(f"Tuple: {checker1.data}, Target: 3 -> Result: {checker1.check_existence(3)}")
    print(f"Tuple: {checker1.data}, Target: 6 -> Result: {checker1.check_existence(6)}")

    checker2 = TupleChecker(('a', 'b', 'c'))
    print(f"\nTuple: {checker2.data}, Target: 'b' -> Result: {checker2.check_existence('b')}")
    print(f"Tuple: {checker2.data}, Target: 'd' -> Result: {checker2.check_existence('d')}")