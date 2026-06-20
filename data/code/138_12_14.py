def generate_truth_table(inputs):
    if not isinstance(inputs, list) or len(inputs) != 1 and len(inputs) != 2:
        raise ValueError("Input must be a list of exactly one or two boolean values.")
    
    num_inputs = len(inputs)
    num_rows = 2 ** num_inputs
    table = []

    for i in range(num_rows):
        row = {}
        for j, input_val in enumerate(inputs):
            if (i >> j) & 1:
                row[f'a{j+1}'] = input_val
            else:
                row[f'a{j+1}'] = not input_val
        row['result'] = eval(''.join([str(row[f'a{i}']) for i in range(1, num_inputs + 1)]), {'and': and_, 'or': or_})
        table.append(row)

    return table

if __name__ == '__main__':
    print(generate_truth_table([True]))
    print(generate_truth_table([False, True]))