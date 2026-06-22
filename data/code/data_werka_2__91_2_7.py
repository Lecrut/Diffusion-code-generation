class BooleanNegator:
    NEGATE_OP = lambda val: not val

    @staticmethod
    def get_negated(is_active: bool) -> bool:
        return BooleanNegator.NEGATE_OP(is_active)

if __name__ == '__main__':
    is_active = True
    result = BooleanNegator.get_negated(is_active)
    print(result)