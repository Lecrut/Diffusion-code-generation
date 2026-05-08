def generate_or_truth_table(bool_list):
    n = len(bool_list)
    table = []
    for i in range(2**n):
        combination = []
        temp = i
        for _ in range(n):
            combination.append(bool(temp % 2))
            temp //= 2
        or_result = False
        for val in combination:
            if val:
                or_result = True
        table.append(tuple(combination) + (or_result,))
    return table
if __name__ == '__main__':
    sample_inputs = [False, True]
    truth_table = generate_or_truth_table(sample_inputs)
    for row in truth_table:
        print(row)