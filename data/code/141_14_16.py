def generate_truth_table(logic_gate):
    return [logic_gate(i, j) for i in range(2) for j in range(2)]

if __name__ == '__main__':
    and_result = lambda x, y: x & y
    or_result = lambda x, y: x | y
    not_result = lambda x: ~x

    and_table = generate_truth_table(and_result)
    or_table = generate_truth_table(or_result)
    not_table = generate_truth_table(not_result)

    print("AND Truth Table:")
    for row in and_table:
        print(row)

    print("\nOR Truth Table:")
    for row in or_table:
        print(row)

    print("\nNOT Truth Table:")
    for row in not_table:
        print(row)