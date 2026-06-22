class BooleanNegator:
    NEGATE_MAP = {True: False, False: True}

    @staticmethod
    def negate(flag):
        return BooleanNegator.NEGATE_MAP.get(flag, not flag)

if __name__ == '__main__':
    is_active = True
    negated_value = BooleanNegator.negate(is_active)
    print(negated_value)