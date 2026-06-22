class NumberSequenceProcessor:
    SEPARATOR = " "

    def __init__(self, raw_input_string):
        self._numbers = self._parse_input(raw_input_string)

    @staticmethod
    def _parse_input(raw):
        if not raw:
            raise ValueError("Input string cannot be empty")
        tokens = raw.split(NumberSequenceProcessor.SEPARATOR)
        return [int(token) for token in tokens if token]

    def get_boundary_values(self):
        if not self._numbers:
            raise ValueError("Processed list cannot be empty")
        return self._numbers[0], self._numbers[-1]

if __name__ == '__main__':
    sample_data = "100 200 300 400 500"
    processor = NumberSequenceProcessor(sample_data)
    first_val, last_val = processor.get_boundary_values()
    print(first_val, last_val)