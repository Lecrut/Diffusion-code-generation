class BoolComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    result = BoolComparator.compare_booleans(True, False)
    print(result)