def print_truth_table():
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'XOR': lambda x, y: x != y
    }
    
    for op_name, operation in operations.items():
        print(f"\nTruth table for {op_name}:")
        for a in [True, False]:
            for b in [True, False]:
                result = operation(a, b)
                print(f"{a} {op_name} {b} = {result}")

if __name__ == '__main__':
    print_truth_table()