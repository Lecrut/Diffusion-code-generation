class BooleanComparer:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> str:
        return 'True' if a == b else 'False'

if __name__ == '__main__':
    comparer = BooleanComparer()
    print(comparer.compare_booleans(True, True))
    print(comparer.compare_booleans(False, False))
    print(comparer.compare_booleans(True, False))