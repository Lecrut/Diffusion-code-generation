def generate_truth_table():
    operations = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'XOR': lambda a, b: a != b
    }
    
    for op_name, operation in operations.items():
        print(f"Truth table for {op_name}:")
        for a in [True, False]:
            for b in [True, False]:
                result = operation(a, b)
                print(f"{a} {op_name} {b} = {result}")

if __name__ == '__main__':
    generate_truth_table()