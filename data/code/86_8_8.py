class BooleanComparator:
    @staticmethod
    def compare(a: bool, b: bool) -> bool:
        return (a and not b) or (not a and b)

if __name__ == '__main__':
    x = True
    y = False
    result = BooleanComparator.compare(x, y)
    print(result)