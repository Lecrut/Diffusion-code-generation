class TruthValueReverser:
    TRUE_MAP = {True: False}
    FALSE_MAP = {False: True}
    VALID_TYPES = (bool,)

    def __init__(self, data_stream):
        self.data_stream = data_stream

    def _validate_and_invert(self, value):
        if not isinstance(value, self.VALID_TYPES):
            raise ValueError(f"Expected boolean, got {type(value).__name__}")
        if value:
            return self.TRUE_MAP[True]
        return self.FALSE_MAP[False]

    def reverse_stream(self):
        for item in self.data_stream:
            yield self._validate_and_invert(item)

def run_reverser():
    initial_values = [True, True, False, False, True, False]
    reverser_instance = TruthValueReverser(initial_values)
    reversed_results = list(reverser_instance.reverse_stream())
    return reversed_results

if __name__ == '__main__':
    computed_output = run_reverser()
    print(computed_output)