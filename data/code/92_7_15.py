class BooleanInverter:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def get_inverse(value: bool) -> bool:
        if value is BooleanInverter.TRUE_VALUE:
            return BooleanInverter.FALSE_VALUE
        return BooleanInverter.TRUE_VALUE

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    print(BooleanInverter.get_inverse(sample_true))
    print(BooleanInverter.get_inverse(sample_false))