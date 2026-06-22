def evaluate_logical_statement(statement: str, values: dict) -> bool:
    OPERATORS = {"AND": lambda a, b: a and b, "OR": lambda a, b: a or b}
    parts = statement.strip().split()
    if len(parts) != 3:
        raise ValueError("Statement must contain exactly two operands and one operator")
    left_key, op, right_key = parts
    if op not in OPERATORS:
        raise ValueError(f"Unsupported operator: {op}")
    if left_key not in values:
        raise ValueError(f"Missing value for variable: {left_key}")
    if right_key not in values:
        raise ValueError(f"Missing value for variable: {right_key}")
    left_val = bool(values[left_key])
    right_val = bool(values[right_key])
    return OPERATORS[op](left_val, right_val)

if __name__ == '__main__':
    sample_values = {"A": True, "B": False}
    sample_statement = "A AND B"
    result = evaluate_logical_statement(sample_statement, sample_values)
    print(result)