class LogicGateEvaluator:
    def __init__(self, inputs):
        self.inputs = inputs
    def evaluate_expression(self, gate_type, input_a, input_b=None):
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
    sample_inputs = {
        "A": 1,
        "B": 0,
        "C": 1
    }
    evaluator = LogicGateEvaluator(sample_inputs)
    print(f"Inputs: A={sample_inputs['A']}, B={sample_inputs['B']}, C={sample_inputs['C']}")
    try:
        result_and = evaluator.evaluate_expression("AND", sample_inputs["A"], sample_inputs["B"])
        print(f"A AND B: {result_and}")
        result_or = evaluator.evaluate_expression("OR", sample_inputs["A"], sample_inputs["C"])
        print(f"A OR C: {result_or}")
        result_not = evaluator.evaluate_expression("NOT", sample_inputs["B"])
        print(f"NOT B: {result_not}")
        result_xor = evaluator.evaluate_expression("XOR", sample_inputs["A"], sample_inputs["B"])
        print(f"A XOR B: {result_xor}")
        try:
            evaluator.evaluate_expression("AND", sample_inputs["A"])
        except ValueError as e:
            print(f"Error caught: {e}")
    except ValueError as e:
        print(f"An error occurred during evaluation: {e}")