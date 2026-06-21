class BooleanProcessor:
    def __init__(self, input_value):
        if not isinstance(input_value, bool):
            raise ValueError("Input must be a boolean")
        self.input_value = input_value

    def get_negated_value(self):
        return not self.input_value

    def get_original_value(self):
        return self.input_value

if __name__ == '__main__':
    samples = [True, False]
    for sample in samples:
        processor = BooleanProcessor(sample)
        print(processor.get_negated_value())
        print(processor.get_original_value())