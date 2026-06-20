class BooleanComparator:
    def __init__(self):
        self.TRUE = True
        self.FALSE = False

    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    result = comparator.compare(True, False)
    print(result)