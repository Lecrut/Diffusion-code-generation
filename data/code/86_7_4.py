class BooleanComparer:
    @staticmethod
    def compare(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparer = BooleanComparer()
    print(comparer.compare(True, True))
    print(comparer.compare(False, False))
    print(comparer.compare(True, False))
    print(comparer.compare(False, True))