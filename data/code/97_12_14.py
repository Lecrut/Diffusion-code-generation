def is_valid_binary(value):
    return value in (0, 1)

def compute_xor(left, right):
    if not is_valid_binary(left):
        raise ValueError(f"Invalid left input: {left}")
    if not is_valid_binary(right):
        raise ValueError(f"Invalid right input: {right}")
    return 1 if left != right else 0

def generate_truth_table():
    inputs = [0, 1]
    rows = []
    for a in inputs:
        for b in inputs:
            result = compute_xor(a, b)
            rows.append((a, b, result))
    return rows

if __name__ == '__main__':
    table_data = generate_truth_table()
    for row in table_data:
        print(f"{row[0]} XOR {row[1]} = {row[2]}")