class LogicGateEvaluator:
    def __init__(self, inputs):
        self.inputs = inputs
    def evaluate(self, gate_type, input_a, input_b=None):
        if gate_type == "AND":
            if input_b is not None:
                return input_a and input_b
            else:
                raise ValueError("AND gate requires two inputs")
        elif gate_type == "OR":
            if input_b is not None:
                return input_a or input_b
            else:
                raise ValueError("OR gate requires two inputs")
        elif gate_type == "NOT":
            if input_b is not None:
                return not input_b
            else:
                raise ValueError("NOT gate requires one input")
        elif gate_type == "XOR":
            if input_b is not None:
                return input_a ^ input_b
            else:
                raise ValueError("XOR gate requires two inputs")
        else:
            raise ValueError(f"Unknown gate type: {gate_type}")
if __name__ == '__main__':
    sample_inputs = [1, 0, 1]
    evaluator = LogicGateEvaluator(sample_inputs)
    print("--- Testing Logic Gates ---")
    try:
        result_and = evaluator.evaluate("AND", 1, 0)
        print(f"1 AND 0 = {result_and}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_and_true = evaluator.evaluate("AND", 1, 1)
        print(f"1 AND 1 = {result_and_true}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_or = evaluator.evaluate("OR", 1, 0)
        print(f"1 OR 0 = {result_or}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_or_true = evaluator.evaluate("OR", 1, 1)
        print(f"1 OR 1 = {result_or_true}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_not = evaluator.evaluate("NOT", 0)
        print(f"NOT 0 = {result_not}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_not_true = evaluator.evaluate("NOT", 1)
        print(f"NOT 1 = {result_not_true}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_xor = evaluator.evaluate("XOR", 1, 0)
        print(f"1 XOR 0 = {result_xor}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_xor_true = evaluator.evaluate("XOR", 1, 1)
        print(f"1 XOR 1 = {result_xor_true}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        evaluator.evaluate("XOR", 1)
    except ValueError as e:
        print(f"Caught expected error for unknown gate: {e}")