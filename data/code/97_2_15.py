def is_valid_input_combination(combination):
    for val in combination:
        if not isinstance(val, int) or val not in [0, 1]:
            return False
    return True

def generate_truth_table(input_combinations):
    results = []
    header = ["A", "B", "C"]
    operations = [
        ("AND", lambda a, b: a & b),
        ("OR", lambda a, b: a | b),
        ("NOT A", lambda a: ~a),
        ("NOT B", lambda b: ~b),
        ("NOT C", lambda c: ~c)
    ]

    for combination in input_combinations:
        if not is_valid_input_combination(combination):
            raise ValueError("Invalid input combination")
        
        result_row = [f"{val}" for val in combination]
        for op_name, func in operations:
            result_row.append(f"{func(*combination)}")
        results.append(result_row)

    return header + list(zip(*results))

def display_truth_table(header, results):
    print("|".join(f"{col:<5}" for col in header))
    print("-" * 20 * len(results[0]))
    for row in results:
        print("|".join(f"{val:^5}" for val in row))

if __name__ == '__main__':
    sample_combinations = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]
    
    table = generate_truth_table(sample_combinations)
    display_truth_table(table[0], table[1:])