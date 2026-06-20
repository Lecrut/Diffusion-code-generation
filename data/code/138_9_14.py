def generate_truth_table():
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
    for x in [True, False]:
        for y in [True, False]:
            result_dict = {op: operations[op](x, y) for op in operations}
            results[(x, y)] = result_dict
    
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)