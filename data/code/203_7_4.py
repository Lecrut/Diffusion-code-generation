class BooleanComparator:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def compare_booleans(a: bool, b: bool) -> int:
        return int(a != b)

if __name__ == '__main__':
    result = BooleanComparator.compare_booleans(True, False)
    print(result)