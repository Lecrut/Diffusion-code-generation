def generate_truth_table(op_name, var1_values, var2_values):
    print(f"Truth Table for {op_name}:")
    print("-" * 30)
    num_rows = len(var1_values)
    for i in range(num_rows):
        val1 = var1_values[i]
        val2 = var2_values[i]
        result = False
        if op_name == "AND":
            result = val1 and val2
        elif op_name == "OR":
            result = val1 or val2
        elif op_name == "NOT_VAR1":
            result = not val1
        else:
            result = "Unknown Operation"
        print(f"({val1}, {val2}) -> {result}")
    print("-" * 30)
if __name__ == '__main__':
    operation = "AND"
    boolean_a_values = [False, True]
    boolean_b_values = [False, True]
    generate_truth_table(operation, boolean_a_values, boolean_b_values)