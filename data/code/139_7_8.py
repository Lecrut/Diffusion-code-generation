class LogicGateEvaluator:
    def __init__(self, inputs):
        self.inputs = inputs
    def evaluate_expression(self, gates):
        result = None
        for gate_index, gate in enumerate(gates):
            if gate == 'AND':
                if len(self.inputs) < 2:
                    raise ValueError("AND gate requires at least two inputs")
                result = self.inputs[gate_index] & self.inputs[gate_index + 1]
            elif gate == 'OR':
                if len(self.inputs) < 2:
                    raise ValueError("OR gate requires at least two inputs")
                result = self.inputs[gate_index] | self.inputs[gate_index + 1]
            elif gate == 'NOT':
                if len(self.inputs) < 1:
                    raise ValueError("NOT gate requires at least one input")
                result = not self.inputs[gate_index]
            else:
                raise ValueError(f"Unknown gate type: {gate}")
        return result
if __name__ == '__main__':
    sample_inputs = [1, 0, 1, 1]
    gates_to_evaluate = ['AND', 'OR', 'NOT']
    evaluator = LogicGateEvaluator(sample_inputs)
    try:
        result = evaluator.evaluate_expression(gates_to_evaluate)
        print(f"Sample Inputs: {sample_inputs}")
        print(f"Gates to evaluate: {gates_to_evaluate}")
        print(f"Evaluation Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")