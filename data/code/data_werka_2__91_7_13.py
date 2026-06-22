class BooleanNegator:
    TRUE_VAL = True
    FALSE_VAL = False

    @staticmethod
    def get_negation(value):
        if value is BooleanNegator.TRUE_VAL:
            return BooleanNegator.FALSE_VAL
        if value is BooleanNegator.FALSE_VAL:
            return BooleanNegator.TRUE_VAL
        raise ValueError("Unsupported input type")

    @classmethod
    def negate_list(cls, lst):
        if len(lst) != 1:
            raise ValueError("List must contain exactly one element")
        element = lst[0]
        return cls.get_negation(element)

if __name__ == '__main__':
    sample_input = [True]
    negator = BooleanNegator()
    output = negator.negate_list(sample_input)
    print(output)