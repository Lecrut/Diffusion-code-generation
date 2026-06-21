def generate_truth_table(n):
    from itertools import product

    variables = [f'v{i}' for i in range(1, n + 1)]
    truth_values = list(product([False, True], repeat=n))
    
    return [{var: val for var, val in zip(variables, row)} for row in truth_values]

if __name__ == '__main__':
    print(generate_truth_table(2))