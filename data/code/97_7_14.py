def generate_truth_table(variables):
    if not isinstance(variables, (list, tuple)):
        raise ValueError("variables must be a list or tuple")
    if len(variables) == 0:
        raise ValueError("variables list cannot be empty")
    for v in variables:
        if not isinstance(v, str) or len(v) == 0:
            raise ValueError("each variable must be a non-empty string")

    n = len(variables)
    num_rows = 1 << n
    table = []

    for i in range(num_rows):
        row = []
        for j in range(n):
            shift = n - 1 - j
            bit = (i >> shift) & 1
            row.append(bool(bit))
        table.append(row)

    return variables, table

def format_table(variables, table):
    header = " | ".join(str(v) for v in variables)
    separator = " | ".join("-" * len(v) for v in variables)
    lines = [header, separator]
    for row in table:
        row_str = " | ".join(str(int(val)) for val in row)
        lines.append(row_str)
    return "\n".join(lines)

if __name__ == '__main__':
    vars_list = ['P', 'Q', 'R']
    variables, table = generate_truth_table(vars_list)
    output = format_table(variables, table)
    print(output)