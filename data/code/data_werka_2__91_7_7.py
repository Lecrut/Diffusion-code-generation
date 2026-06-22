class BooleanNegator:
    TRUE_VAL = True
    FALSE_VAL = False

    @staticmethod
    def get_negation(value):
        if value is BooleanNegator.TRUE_VAL:
            return BooleanNegator.FALSE_VAL
        if value is BooleanNegator.FALSE_VAL:
            return BooleanNegator.TRUE_VAL
        raise ValueError("Input must be a boolean")

    @staticmethod
    def process_list(input_list):
        if len(input_list) != 1:
            raise ValueError("List must contain exactly one element")
        element = input_list[0]
        return BooleanNegator.get_negation(element)

if __name__ == '__main__':
    sample_input = [True]
    output = BooleanNegator.process_list(sample_input)
    print(output)