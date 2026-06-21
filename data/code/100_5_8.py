class LogicSystem:
    EXPECTED_OPERATOR = "and"

    def __init__(self, operation_type):
        if operation_type != self.EXPECTED_OPERATOR:
            raise ValueError(f"Unsupported operation: {operation_type}")
        self.operation = operation_type

    def evaluate(self, val1, val2):
        if not isinstance(val1, bool) or not isinstance(val2, bool):
            raise ValueError("Inputs must be boolean")
        if self.operation == "and":
            return bool(val1 and val2)
        return False

def verify_logic(input_a, input_b):
    system = LogicSystem("and")
    return system.evaluate(input_a, input_b)

if __name__ == '__main__':
    a_val = True
    b_val = False
    output = verify_logic(a_val, b_val)
    print(output)