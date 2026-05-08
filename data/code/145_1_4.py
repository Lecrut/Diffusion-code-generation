def test_nested_logic(test_cases):
    results = {}
    for name, logic in test_cases.items():
        expected = logic['expected']
        actual = logic['actual']
        results[name] = {'expected': expected, 'actual': actual}
    return results
if __name__ == '__main__':
    sample_test_data = {
        "test_case_1": {
            "expression": "A and (B or C)",
            "inputs": {"A": True, "B": False, "C": True},
            "expected": True,
            "actual": True
        },
        "test_case_2": {
            "expression": "not (A and B)",
            "inputs": {"A": True, "B": True},
            "expected": False,
            "actual": False
        },
        "test_case_3": {
            "expression": "(A or B) and C",
            "inputs": {"A": False, "B": False, "C": True},
            "expected": False,
            "actual": False
        },
        "test_case_4": {
            "expression": "A or B or C",
            "inputs": {"A": True, "B": False, "C": False},
            "expected": True,
            "actual": True
        }
    }
    def evaluate_boolean_expression(expression, inputs):
        if expression == "A and (B or C)":
            return inputs.get("A", False) and (inputs.get("B", False) or inputs.get("C", False))
        elif expression == "not (A and B)":
            return not (inputs.get("A", False) and inputs.get("B", False))
        elif expression == "(A or B) and C":
            return (inputs.get("A", False) or inputs.get("B", False)) and inputs.get("C", False)
        elif expression == "A or B or C":
            return inputs.get("A", False) or inputs.get("B", False) or inputs.get("C", False)
        else:
            raise ValueError("Unknown expression")
    processed_test_cases = {}
    for name, data in sample_test_data.items():
        expression = data["expression"]
        inputs = data["inputs"]
        expected = data["expected"]
        actual = evaluate_boolean_expression(expression, inputs)
        processed_test_cases[name] = {
            "expression": expression,
            "inputs": inputs,
            "expected": expected,
            "actual": actual
        }
    results = test_nested_logic(processed_test_cases)
    import json
    print(json.dumps(results, indent=4))