class AndGateValidator:
    INPUT_A = 1
    INPUT_B = 0
    EXPECTED_OUTPUT = 0

    @staticmethod
    def check_and_gate(a, b):
        return a and b == True

if __name__ == '__main__':
    validator = AndGateValidator()
    result = validator.check_and_gate(AndGateValidator.INPUT_A, AndGateValidator.INPUT_B)
    print(f"Input A: {AndGateValidator.INPUT_A}")
    print(f"Input B: {AndGateValidator.INPUT_B}")
    print(f"Expected AND result: {AndGateValidator.EXPECTED_OUTPUT}")
    print(f"Actual AND result: {result}")
    if result:
        print("Gate validity: Valid")
    else:
        print("Gate validity: Invalid")