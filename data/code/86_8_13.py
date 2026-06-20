class BooleanComparator:
    @staticmethod
    def compare(a: bool, b: bool) -> bool:
        return a != b

if __name__ == '__main__':
    x = True
    y = False
    comparator = BooleanComparator()
    result = comparator.compare(x, y)
    print(result)