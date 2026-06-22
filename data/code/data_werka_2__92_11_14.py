class BooleanStringInverter:
    def __init__(self):
        self.true_values = {'true', '1', 'yes', 't'}
        self.false_values = {'false', '0', 'no', 'f'}

    def invert(self, raw_input: str) -> str:
        normalized = raw_input.strip().lower()
        if normalized in self.true_values:
            return 'False'
        if normalized in self.false_values:
            return 'True'
        raise ValueError(f"Invalid boolean string: {raw_input}")

if __name__ == '__main__':
    inverter = BooleanStringInverter()
    print(inverter.invert('True'))
    print(inverter.invert('false'))
    print(inverter.invert('  YES  '))
    print(inverter.invert('0'))
    print(inverter.invert('No'))
    print(inverter.invert('1'))