class LogicGateEvaluator:
    def __init__(self, inputs):
        self.inputs = inputs
    def evaluate_expression(self, gates):
        results = {}
        for gate_name, gate_func in gates.items():
            if gate_name == "AND":
                results[gate_name] = self.inputs[0] & self.inputs[1]
            elif gate_name == "OR":
                results[gate_name] = self.inputs[0] | self.inputs[1]
            elif gate_name == "NOT":
                results[gate_name] = not self.inputs[0]
            elif gate_name == "XOR":
                results[gate_name] = self.inputs[0] ^ self.inputs[1]
            else:
                results[gate_name] = None
        return results
if __name__ == '__main__':
    sample_inputs = [1, 0, 1]
    gates_to_evaluate = {
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "NOT": lambda a: not a,
        "XOR": lambda a, b: a ^ b
    }
    evaluator = LogicGateEvaluator(sample_inputs)
    evaluation_results = evaluator.evaluate_expression(gates_to_evaluate)
    print(evaluation_results)