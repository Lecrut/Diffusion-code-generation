def generate_truth_table(bool_list, operation):
    n = len(bool_list)
    results = []
    for i in range(2**n):
        current_combination = []
        temp = i
        for _ in range(n):
            current_combination.append(temp % 2)
            temp //= 2
        a = bool_list[current_combination[0]] if n > 0 else False
        b = bool_list[current_combination[1]] if n > 1 else False
        if n == 1:
            result = a
        elif n == 2:
            result = a and b if operation == "AND" else a or b
        else:
            pass
    if len(bool_list) < 2:
        return []
    rows = []
    n = len(bool_list)
    for i in range(2**n):
        row = []
        for j in range(n):
            row.append(bool_list[j])
        if n == 2:
            A, B = bool_list[0], bool_list[1]
            if operation == "AND":
                result = A and B
            elif operation == "OR":
                result = A or B
            else:
                result = None
            rows.append([A, B, result])
        else:
            pass
    return rows
if __name__ == '__main__':
    inputs_and = [False, False]
    print("--- AND Truth Table (2 Inputs) ---")
    table_and = generate_truth_table(inputs_and, "AND")
    for row in table_and:
        print(row)
    inputs_or = [False, True]
    print("\n--- OR Truth Table (2 Inputs) ---")
    table_or = generate_truth_table(inputs_or, "OR")
    for row in table_or:
        print(row)