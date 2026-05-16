def evaluate_nested_logic(inputs, expressions):
    results = {}
    input_map = {key: value for key, value in inputs.items()}
    for expr in expressions:
        if expr == "":
            results[expr] = False
            continue
        tokens = expr.split()
        def evaluate_token(token):
            if token in input_map:
                return input_map[token]
            raise ValueError(f"Undefined variable: {token}")
        def evaluate_expression(tokens):
            if len(tokens) == 1:
                token = tokens[0]
                return evaluate_token(token)
            if len(tokens) == 3:
                op1 = evaluate_expression(tokens[:2])
                op = tokens[2]
                op2 = evaluate_expression(tokens[3:])
                if op == "and":
                    return op1 and op2
                elif op == "or":
                    return op1 or op2
                elif op == "not":
                    return not op1
                else:
                    raise ValueError(f"Unknown operator: {op}")
            raise ValueError(f"Invalid expression structure: {expr}")
        try:
            results[expr] = evaluate_expression(tokens)
        except ValueError as e:
            results[expr] = f"Error: {e}"
        except Exception as e:
            results[expr] = f"Unexpected Error: {e}"
    return results
if __name__ == '__main__':
    sample_inputs = {
        "A": True,
        "B": False,
        "C": True
    }
    sample_expressions = [
        "A",
        "B or C",
        "not A",
        "A and B",
        "not (A or B)",
        "C and not A"
    ]
    calculated_results = evaluate_nested_logic(sample_inputs, sample_expressions)
    print(calculated_results)