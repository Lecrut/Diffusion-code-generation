class NumberSequenceProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def _parse_input(self):
        if isinstance(self.data_source, str):
            tokens = self.data_source.split()
            return [int(token) for token in tokens]
        if isinstance(self.data_source, (list, tuple)):
            return list(self.data_source)
        raise ValueError("Unsupported data source type")

    def get_boundary_values(self):
        numbers = self._parse_input()
        if not numbers:
            raise ValueError("Sequence cannot be empty")
        return numbers[0], numbers[-1]

if __name__ == '__main__':
    raw_input = "5 12 19 26 33"
    processor = NumberSequenceProcessor(raw_input)
    first_val, last_val = processor.get_boundary_values()
    print(first_val, last_val)