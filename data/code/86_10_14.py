class BooleanComparer:
    EQUAL = 'Equal'
    DIFFERENT = 'Different'

    @staticmethod
    def compare_booleans(a: bool, b: bool) -> str:
        return BooleanComparer.EQUAL if a == b else BooleanComparer.DIFFERENT

if __name__ == '__main__':
    print(BooleanComparer.compare_booleans(True, True))
    print(BooleanComparer.compare_booleans(False, False))
    print(BooleanComparer.compare_booleans(True, False))
    print(BooleanComparer.compare_booleans(False, True))