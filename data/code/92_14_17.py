class BooleanInverter:
    def __init__(self, initial_value=False):
        self.current_value = initial_value

    def invert(self):
        self.current_value = not self.current_value
        return self.current_value

    def get(self):
        return self.current_value

    def set_value(self, new_value):
        if not isinstance(new_value, bool):
            raise ValueError("Input must be a boolean value")
        self.current_value = new_value
        return self.current_value

if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.get())
    print(inverter.invert())
    print(inverter.invert())
    inverter.set_value(False)
    print(inverter.get())
    print(inverter.invert())