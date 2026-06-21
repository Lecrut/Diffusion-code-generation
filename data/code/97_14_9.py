def validate_operand(value):
    if not isinstance(value, bool):
        raise ValueError(f"Expected bool, got {type(value)}")
    return value

def compute_or_result(left, right):
    validate_operand(left)
    validate_operand(right)
    return left or right

def build_or_truth_table():
    operands = [True, False]
    table = []
    for p in operands:
        for q in operands:
            result = compute_or_result(p, q)
            table.append({"p": p, "q": q, "p OR q": result})
    return table

if __name__ == '__main__':
    result = build_or_truth_table()
    print(result)