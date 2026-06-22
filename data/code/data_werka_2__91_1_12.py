class BooleanLogicProcessor:
    TRUE_STATE = True
    FALSE_STATE = False

    @classmethod
    def invert_flag(cls, flag: bool) -> bool:
        return not flag

    @staticmethod
    def verify_negation(original: bool, negated: bool) -> bool:
        return original != negated

if __name__ == '__main__':
    input_true = True
    input_false = False

    result_true = BooleanLogicProcessor.invert_flag(input_true)
    result_false = BooleanLogicProcessor.invert_flag(input_false)

    print(result_true)
    print(result_false)

    print(BooleanLogicProcessor.verify_negation(input_true, result_true))
    print(BooleanLogicProcessor.verify_negation(input_false, result_false))