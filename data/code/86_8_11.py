class BooleanComparator:
    @staticmethod
    def compare(a: bool, b: bool) -> bool:
        return a != b

if __name__ == '__main__':
    comparator = BooleanComparator()
    x = True
    y = False
    result = comparator.compare(x, y)
    print(result)