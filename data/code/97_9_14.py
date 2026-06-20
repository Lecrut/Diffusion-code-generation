def generate_truth_table(a, b):
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'XOR': lambda x, y: x != y,
        'NOT A': lambda x: not x,
        'NOT B': lambda x, y: not y
    }
    
    print("A | B | AND | OR | XOR | NOT A | NOT B")
    for a_val in [True, False]:
        for b_val in [True, False]:
            row = [a_val, b_val]
            for operation_name, operation in operations.items():
                if 'NOT' in operation_name:
                    result = operation(operation_name == 'NOT A', operation_name == 'NOT B')
                else:
                    result = operation(a_val, b_val)
                row.append(result)
            print(" | ".join(map(str, row)))

if __name__ == '__main__':
    generate_truth_table(True, False)