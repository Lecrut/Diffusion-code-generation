def generate_truth_table(n):
    from itertools import product

    variables = [chr(97 + i) for i in range(n)]
    truth_values = list(product([0, 1], repeat=n))
    
    table = []
    for values in truth_values:
        row = {variables[i]: values[i] for i in range(n)}
        table.append(row)
    
    return table

if __name__ == '__main__':
    print(generate_truth_table(2))