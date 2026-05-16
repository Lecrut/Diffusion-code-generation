class LogicGateEvaluator:
    def __init__(self, inputs):
        self.inputs = inputs
    def evaluate_expression(self, gate_type, input1, input2=None):
        if gate_type == "AND":
            return input1 and input2
        elif gate_type == "OR":
            return input1 or input2
        elif gate_type == "NOT":
            return not input1
        elif gate_type == "XOR":
            return input1 ^ input2
        else:
            raise ValueError("Unknown gate type")
if __name__ == '__main__':
    sample_inputs = {
        "A": 1,
        "B": 0,
        "C": 1
    }
    evaluator = LogicGateEvaluator(sample_inputs)
    print("--- Testing AND Gate ---")
    result_and = evaluator.evaluate_expression("AND", sample_inputs["A"], sample_inputs["B"])
    print(f"A AND B: {result_and}")
    print("\n--- Testing OR Gate ---")
    result_or = evaluator.evaluate_expression("OR", sample_inputs["A"], sample_inputs["C"])
    print(f"A OR C: {result_or}")
    print("\n--- Testing NOT Gate ---")
    result_not = evaluator.evaluate_expression("NOT", sample_inputs["B"])
    print(f"NOT B: {result_not}")
    print("\n--- Testing XOR Gate ---")
    result_xor = evaluator.evaluate_expression("XOR", sample_inputs["A"], sample_inputs["C"])
    print(f"A XOR C: {result_xor}")