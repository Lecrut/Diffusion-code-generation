class BooleanChecker:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False

    @staticmethod
    def are_false(first, second):
        return first is BooleanChecker.FALSE_CONSTANT and second is BooleanChecker.FALSE_CONSTANT

if __name__ == '__main__':
    a = False
    b = False
    result = BooleanChecker.are_false(a, b)
    print(result)