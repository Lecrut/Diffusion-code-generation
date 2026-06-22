class BooleanInverter:
    def __init__(self):
        self.true_mappings = frozenset(['true', '1', 'yes', 'y'])
        self.false_mappings = frozenset(['false', '0', 'no', 'n'])
        self.true_output = 'False'
        self.false_output = 'True'

    def invert(self, raw_input: str) -> str:
        cleaned = raw_input.strip().lower()
        if cleaned in self.true_mappings:
            return self.false_output
        if cleaned in self.false_mappings:
            return self.true_output
        raise ValueError(f"Unrecognized boolean string: {raw_input}")

    def invert_list(self, inputs: list) -> list:
        return [self.invert(item) for item in inputs]

if __name__ == '__main__':
    inverter = BooleanInverter()
    result1 = inverter.invert('True')
    print(result1)
    result2 = inverter.invert('FALSE')
    print(result2)
    result3 = inverter.invert('YES')
    print(result3)
    result4 = inverter.invert('0')
    print(result4)
    results = inverter.invert_list(['1', 'No', 'Y'])
    for r in results:
        print(r)