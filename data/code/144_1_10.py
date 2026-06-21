def generate_truth_table(n):
    if n <= 0:
        return []
    
    variables = [i for i in range(n)]
    truth_values = [False, True]
    table = []
    
    def helper(var_index, current_row):
        if var_index == len(variables):
            table.append(current_row.copy())
            return
        
        for value in truth_values:
            current_row[variables[var_index]] = value
            helper(var_index + 1, current_row)
    
    helper(0, {})
    return table

if __name__ == '__main__':
    sample_table = generate_truth_table(3)
    print(sample_table)