def generate_truth_table(conditions):
    if not all(isinstance(cond, str) and len(cond) == 1 for cond in conditions):
        raise ValueError("All conditions must be single character strings.")
    
    num_conditions = len(conditions)
    num_rows = 2 ** num_conditions
    
    print(f"Truth Table for {', '.join(conditions)}:")
    for i in range(num_rows):
        row_data = []
        for j in range(num_conditions):
            if (i >> j) & 1:
                row_data.append('1')
            else:
                row_data.append('0')
        print(" ".join(row_data))

if __name__ == '__main__':
    inputs = ['P', 'Q']
    generate_truth_table(inputs)