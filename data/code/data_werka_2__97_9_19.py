def generate_truth_table(a: bool, b: bool) -> None:
    operators = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NAND': lambda x, y: not (x and y),
        'NOR': lambda x, y: not (x or y),
        'XOR': lambda x, y: x != y,
    }
    op_names = list(operators.keys())
    header = "A     B     " + "     ".join(op_names)
    separator = "-" * len(header)
    print(separator)
    print(header)
    print(separator)
    for val_a in [True, False]:
        for val_b in [True, False]:
            row_vals = [str(val_a), str(val_b)]
            for op_name in op_names:
                op_func = operators[op_name]
                res = op_func(val_a, val_b)
                row_vals.append(str(res))
            print("     ".join(row_vals))
    print(separator)

if __name__ == '__main__':
    input_a = True
    input_b = False
    generate_truth_table(input_a, input_b)