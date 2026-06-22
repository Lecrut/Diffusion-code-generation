def compute_logic(a, b, c, d):
    return (a and b) or (c and d)

def format_row(values, result):
    parts = [str(v) for v in values]
    parts.append(str(result))
    return ' | '.join(f"{p:<5}" for p in parts)

def generate_truth_table():
    num_inputs = 4
    input_names = ['A', 'B', 'C', 'D']
    total_rows = 1 << num_inputs
    header = ' | '.join(f"{name:<5}" for name in input_names)
    header += " | Result"
    print(header)
    separator = '-' * (5 * num_inputs + 2 * (num_inputs - 1) + 10)
    print(separator)
    for i in range(total_rows):
        values = []
        for j in range(num_inputs):
            bit_index = num_inputs - 1 - j
            val = (i >> bit_index) & 1
            values.append(bool(val))
        result = compute_logic(*values)
        print(format_row(values, result))

if __name__ == '__main__':
    generate_truth_table()