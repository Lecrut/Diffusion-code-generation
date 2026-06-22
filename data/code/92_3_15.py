class BooleanNegator:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def _get_opposite(value):
        return BooleanNegator.FALSE_VALUE if value else BooleanNegator.TRUE_VALUE

    def negate_all(self, values):
        return [self._get_opposite(v) for v in values]

if __name__ == '__main__':
    negator = BooleanNegator()
    sample_data = [True, True, False, False, True]
    output = negator.negate_all(sample_data)
    print(output)