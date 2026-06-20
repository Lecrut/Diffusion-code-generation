def generate_truth_table(a, b):
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'XOR': lambda x, y: x != y,
        'NOT A': lambda x: not x,
        'NOT B': lambda x, y: not y
    }
    
    header = "A | B | AND | OR | XOR | NOT A | NOT B"
    print(header)
    for a_val in [True, False]:
        for b_val in [True, False]:
            row = f"{a_val} | {b_val} | "
            for operation in operations.values():
                if callable(operation):
                    result = operation(a_val, b_val) if 'B' in operation.__name__ else operation(a_val)
                    row += f"{result} | "
            print(row.strip())

if __name__ == '__main__':
    generate_truth_table(True, False)