def format_truth_table(input_names, operation_func):
    n = len(input_names)
    if n == 0:
        return ""
    
    num_rows = 1 << n
    header = " | ".join(input_names)
    sep = "-" * len(header)
    
    lines = [header, sep]
    
    for i in range(num_rows):
        current_inputs = {}
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            current_inputs[input_names[j]] = bool(bit)
        
        row_values = [str(current_inputs[name]) for name in input_names]
        result = operation_func(current_inputs)
        row_values.append(str(bool(result)))
        
        lines.append(" | ".join(row_values))
    
    return "\n".join(lines)

if __name__ == '__main__':
    inputs = ["P", "Q"]
    def and_op(args):
        return args["P"] and args["Q"]
    
    table_str = format_truth_table(inputs, and_op)
    print(table_str)