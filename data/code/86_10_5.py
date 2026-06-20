class BooleanComparer:
    EQUAL_MESSAGE = 'Equal'
    DIFFERENT_MESSAGE = 'Different'

    @staticmethod
    def compare_booleans(a: bool, b: bool) -> str:
        if a == b:
            return BooleanComparer.EQUAL_MESSAGE
        else:
            return BooleanComparer.DIFFERENT_MESSAGE

if __name__ == '__main__':
    print(BooleanComparer.compare_booleans(True, True))
    print(BooleanComparer.compare_booleans(False, False))
    print(BooleanComparer.compare_booleans(True, False))
    print(BooleanComparer.compare_booleans(False, True))