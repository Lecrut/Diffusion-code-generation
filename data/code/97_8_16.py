def generate_truth_table(a, b):
    truth_table = {
        'A': [a],
        'B': [b]
    }
    for i in range(1, 2):
        truth_table['A'].append(not a)
        truth_table['B'].append(b)
    return truth_table

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    table = generate_truth_table(sample_a, sample_b)
    print(f"Truth Table for A={sample_a} and B={sample_b}:")
    headers = " | ".join(table.keys())
    print("-" * len(headers))
    print(headers)
    print("-" * len(headers))
    for a_val, b_val in zip(table['A'], table['B']):
        print(f"{a_val} | {b_val}")