def generate_truth_table(n):
    from itertools import product

    variables = [chr(97 + i) for i in range(n)]
    truth_values = list(product([0, 1], repeat=n))
    table = [{var: val for var, val in zip(variables, row)} for row in truth_values]
    return table

if __name__ == '__main__':
    sample_table = generate_truth_table(3)
    print(sample_table)