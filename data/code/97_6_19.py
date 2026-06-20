def print_truth_table(input_tuples):
    if not all(isinstance(tup, tuple) and len(tup) == 2 for tup in input_tuples):
        raise ValueError("All inputs must be tuples of length 2.")
    
    headers = ['P', 'Q']
    table_data = []

    for p, q in input_tuples:
        row_data = [p, q]
        table_data.append(row_data)

    print(f"{' | '.join(headers)}")
    print('-' * (len(headers) * 3 - 1))
    for row in table_data:
        print(f" {' | '.join(map(str, row))}")

if __name__ == '__main__':
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print_truth_table(inputs)