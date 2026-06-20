def boolean_operations():
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NOT': lambda x: not x,
        'XOR': lambda x, y: x != y,
        'NAND': lambda x, y: not (x and y),
        'NOR': lambda x, y: not (x or y),
        'IMPLIES': lambda x, y: not x or y
    }
    
    results = {}
    for x in [False, True]:
        for y in [False, True]:
            result_row = {}
            for op_name, op_func in operations.items():
                result_row[op_name] = op_func(x, y)
            results[(x, y)] = result_row
    
    return results

if __name__ == '__main__':
    truth_table = boolean_operations()
    sample_values = {(False, False): 'AND', (True, True): 'OR'}
    for inputs, operation in sample_values.items():
        print(f"Truth table for {operation} with inputs {inputs}:")
        print(truth_table[inputs][operation])