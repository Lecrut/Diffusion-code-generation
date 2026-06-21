class BooleanInverter:
    def __init__(self):
        self.supported_types = (bool,)

    @classmethod
    def invert(cls, flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        return not flag

if __name__ == '__main__':
    inverter = BooleanInverter()
    result_true = BooleanInverter.invert(True)
    result_false = BooleanInverter.invert(False)
    print(result_true)
    print(result_false)