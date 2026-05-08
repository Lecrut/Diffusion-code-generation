def generate_truth_table(num_vars, expression):
    if num_vars <= 0:
        return "Number of variables must be positive."
    num_rows = 2**num_vars
    truth_table = []
    for i in range(num_rows):
        row_values = []
        for j in range(num_vars):
            bit = (i >> j) & 1
            row_values.append(str(bit))
        row_str = " ".join(row_values)
        if expression == "AND":
            result = True
            for val in [int(v) for v in row_values]:
                if val == 0:
                    result = False
                    break
            truth_table.append((row_str, str(result)))
        elif expression == "OR":
            result = False
            for val in [int(v) for v in row_values]:
                if val == 1:
                    result = True
                    break
            truth_table.append((row_str, str(result)))
        elif expression == "NOT":
            if num_vars >= 1:
                first_var = int(row_values[0])
                result = not first_var
                truth_table.append((row_str, str(result)))
            else:
                truth_table.append((row_str, "Error: NOT requires at least one variable."))
        else:
            truth_table.append((row_str, "Expression not supported."))
    header = [f"V1", f"V2", f"V3", f"V4"]
    table_output = [header]
    for row, result in truth_table:
        table_output.append([row, result])
    return "\n".join([", ".join(table_output[0]), "\n" + "\n".join([", ".join(table_output[i]) for i in range(1, len(table_output))])])
if __name__ == '__main__':
    num_vars = 2
    expression = "AND"
    print(generate_truth_table(num_vars, expression))
    num_vars = 3
    expression = "OR"
    print(generate_truth_table(num_vars, expression))
    num_vars = 2
    expression = "NOT"
    print(generate_truth_table(num_vars, expression))