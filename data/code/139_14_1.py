def generate_truth_tables():
    and_table = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    or_table = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    not_table = [
        [0],
        [1]
    ]
    xor_table = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    truth_tables = {
        "AND": and_table,
        "OR": or_table,
        "NOT": not_table,
        "XOR": xor_table
    }
    return truth_tables
if __name__ == '__main__':
    tables = generate_truth_tables()
    print(tables)