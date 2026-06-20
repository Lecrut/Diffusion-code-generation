def generate_or_truth_table(a_values, b_values):
    return [{'a': a, 'b': b, 'a OR b': a or b} for a in a_values for b in b_values]

if __name__ == '__main__':
    inputs = [True, False]
    truth_table = generate_or_truth_table(inputs, inputs)
    print("a | b | a OR b")
    for row in truth_table:
        print(f"{row['a']} | {row['b']} | {row['a OR b']}")