class BooleanComparator:
    def __init__(self, expr1: bool, expr2: bool):
        self.expr1 = expr1
        self.expr2 = expr2

    def compare(self) -> str:
        if self.expr1 == self.expr2:
            return "Identical"
        else:
            return "Different"

if __name__ == '__main__':
    comparator = BooleanComparator((5 > 3) and (10 == 10), True)
    print(comparator.compare())