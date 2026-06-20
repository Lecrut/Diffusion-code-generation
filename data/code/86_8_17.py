class BoolComparator:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b
    
    def compare(self) -> bool:
        return self.a != self.b

if __name__ == '__main__':
    comparator = BoolComparator(True, False)
    print(comparator.compare())