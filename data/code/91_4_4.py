class BooleanHandler:
    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        self.value = value

    def negate(self):
        return not self.value

    def get_value(self):
        return self.value

if __name__ == '__main__':
    handler = BooleanHandler(True)
    print(handler.negate())
    print(handler.get_value())