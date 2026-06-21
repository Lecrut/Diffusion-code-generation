class BooleanInverter:
    def __init__(self, input_value):
        if not isinstance(input_value, bool):
            raise ValueError("Input must be a boolean")
        self.input_value = input_value

    def invert(self):
        return not self.input_value

def negate_boolean(value):
    inverter = BooleanInverter(value)
    return inverter.invert()

if __name__ == '__main__':
    value1 = True
    value2 = False
    result1 = negate_boolean(value1)
    result2 = negate_boolean(value2)
    print(result1)
    print(result2)
    instance = BooleanInverter(True)
    print(instance.invert())
    instance = BooleanInverter(False)
    print(instance.invert())