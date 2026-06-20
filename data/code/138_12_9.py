def generate_truth_table(inputs):
    if not isinstance(inputs, list) or len(inputs) == 0:
        raise ValueError("Input must be a non-empty list of boolean values.")

    num_inputs = len(inputs)
    num_rows = 2 ** num_inputs
    table = []
    
    for i in range(num_rows):
        row = {}
        for j in range(num_inputs):
            if (i >> j) & 1:
                row[f'a{j+1}'] = inputs[j]
            else:
                row[f'a{j+1}'] = not inputs[j]
        table.append({'a': row['a1'], 'b': row.get('a2', None), 'result': row.get('a3', None)})

    return table

if __name__ == '__main__':
    sample_values = generate_truth_table([True, False])
    print(sample_values)