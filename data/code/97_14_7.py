def generate_or_truth_table():
    input_values = [True, False]
    truth_table = []
    for a in input_values:
        for b in input_values:
            or_result = a or b
            truth_table.append({'a': a, 'b': b, 'or_result': or_result})
    return truth_table

if __name__ == '__main__':
    or_truth_table = generate_or_truth_table()
    print("a | b | a OR b")
    print("---|---|--------")
    for row in or_truth_table:
        print(f"{row['a']} | {row['b']} | {row['or_result']}")