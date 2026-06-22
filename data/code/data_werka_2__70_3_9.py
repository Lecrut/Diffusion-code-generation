class NumberSequenceProcessor:
    def __init__(self, values):
        self.values = list(values)

    def get_first(self):
        if not self.values:
            raise ValueError("Sequence is empty")
        return self.values[0]

    def get_last(self):
        if not self.values:
            raise ValueError("Sequence is empty")
        return self.values[-1]

    def get_boundary_pair(self):
        return self.get_first(), self.get_last()

if __name__ == '__main__':
    raw_input = "5 12 19 26 33"
    parsed_numbers = [int(x) for x in raw_input.split()]
    processor = NumberSequenceProcessor(parsed_numbers)
    print(processor.get_first())
    print(processor.get_last())
    print(processor.get_boundary_pair())