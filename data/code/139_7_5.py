class LogicGateEvaluator:
    def __init__(self, gate_definitions):
        self.gate_definitions = gate_definitions
    def evaluate(self, inputs, gates):
        results = {}
        for gate_name, definition in gates.items():
            if gate_name == "AND":
                results[gate_name] = inputs[definition['A']] & inputs[definition['B']]
            elif gate_name == "OR":
                results[gate_name] = inputs[definition['A']] | inputs[definition['B']]
            elif gate_name == "NOT":
                results[gate_name] = not inputs[definition['A']]
            elif gate_name == "XOR":
                results[gate_name] = inputs[definition['A']] ^ inputs[definition['B']]
            else:
                results[gate_name] = None
        return results
if __name__ == '__main__':
    gate_definitions = {
        "AND": {"A": "input1", "B": "input2"},
        "OR": {"A": "input1", "B": "input2"},
        "NOT": {"A": "input1"},
        "XOR": {"A": "input1", "B": "input2"}
    }
    sample_inputs = {
        "input1": 1,
        "input2": 0
    }
    evaluator = LogicGateEvaluator(gate_definitions)
    gates_to_evaluate = {
        "AND": gate_definitions["AND"],
        "OR": gate_definitions["OR"],
        "NOT": gate_definitions["NOT"],
        "XOR": gate_definitions["XOR"]
    }
    evaluation_results = evaluator.evaluate(sample_inputs, gates_to_evaluate)
    print(evaluation_results)