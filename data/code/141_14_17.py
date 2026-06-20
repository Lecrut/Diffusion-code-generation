def generate_truth_tables():
    truth_table_and = [[i & j for j in range(2)] for i in range(2)]
    truth_table_or = [[i | j for j in range(2)] for i in range(2)]
    truth_table_not = [[~i, ~j] for i in range(2) for j in range(2)]
    return truth_table_and, truth_table_or, truth_table_not

if __name__ == '__main__':
    and_table, or_table, not_table = generate_truth_tables()
    print("AND Truth Table:")
    for row in and_table:
        print(row)
    print("\nOR Truth Table:")
    for row in or_table:
        print(row)
    print("\nNOT Truth Table:")
    for row in not_table:
        print(row)