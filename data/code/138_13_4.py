def generate_truth_table(bool_list, operation):
    n = len(bool_list)
    table = []
    for i in range(2**n):
        row = []
        for j in range(n):
            if (i >> j) & 1:
                row.append(bool_list[j])
            else:
                row.append(not bool_list[j])
        result = None
        if operation == "AND":
            result = all(row)
        elif operation == "OR":
            result = any(row)
        else:
            raise ValueError("Unsupported operation")
        table.append(row + [result])
    return table
if __name__ == '__main__':
    input_bools = [False, True]
    operation_type = "AND"
    truth_table = generate_truth_table(input_bools, operation_type)
    for row in truth_table:
        print(row)