def generate_truth_table(var1_values, var2_values):
    table = []
    for v1 in var1_values:
        for v2 in var2_values:
            table.append((v1, v2))
    return table

if __name__ == '__main__':
    var1 = [0, 1]
    var2 = [0, 1]
    truth_table = generate_truth_table(var1, var2)
    for row in truth_table:
        print(row)