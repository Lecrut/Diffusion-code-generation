class AndGate:
    EXPECTED_OUTPUT = 0

    @staticmethod
    def evaluate(a, b):
        return a and b

    @classmethod
    def check_validity(cls, a, b):
        result = cls.evaluate(a, b)
        is_valid = result == cls.EXPECTED_OUTPUT
        return result, is_valid

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    actual_output, is_valid = AndGate.check_validity(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Expected AND result: {AndGate.EXPECTED_OUTPUT}")
    print(f"Actual AND result: {actual_output}")
    if is_valid:
        print("Gate validity: Valid")
    else:
        print("Gate validity: Invalid")