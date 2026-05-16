def evaluate_expression(expression, var1_name, var2_name, truth_table):
    var1_val = truth_table[truth_table.index(truth_table[0])]
    var2_val = truth_table[truth_table.index(truth_table[1])]
    if "AND" in expression:
        result = var1_val and var2_val
    elif "OR" in expression:
        result = var1_val or var2_val
    elif "NOT" in expression:
        if var1_name == "A":
            result = not var1_val
        else:
            result = False
    else:
        result = var1_val
    truth_table[truth_table.index(truth_table[0])][3] = result
def generate_truth_table(expression, var1_name, var2_name, num_rows):
    truth_table = []
    for i in range(2**num_rows):
        row = []
        for j in range(num_rows):
            var1_val = (i >> j) & 1
            var2_val = (i >> (j + 1)) & 1
            if var1_name == "A":
                val1 = bool(var1_val)
            elif var2_name == "B":
                val2 = bool(var2_val)
            else:
                val1 = var1_val
                val2 = var2_val
            row.append(val1)
        A = (i >> 0) & 1
        B = (i >> 1) & 1
        result = False
        if "A" in expression:
            A_val = A
        else:
            A_val = False
        if "B" in expression:
            B_val = B
        else:
            B_val = False
        if "AND" in expression:
            result = A_val and B_val
        elif "OR" in expression:
            result = A_val or B_val
        elif "NOT" in expression:
            if "A" in expression:
                result = not A_val
            elif "B" in expression:
                result = not B_val
        else:
            result = A_val                                
        row.append(result)
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    expression = "A AND B OR NOT A"
    var1_name = "A"
    var2_name = "B"
    num_rows = 4
    truth_table_result = generate_truth_table(expression, var1_name, var2_name, num_rows)
    print(f"Truth Table for Expression: {expression}")
    print(f"Variables: {var1_name}, {var2_name}\n")
    header = f"{var1_name}\t{var2_name}\tResult"
    print(header)
    print("-" * len(header))
    for row in truth_table_result:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")