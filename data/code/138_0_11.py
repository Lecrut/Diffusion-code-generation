def generate_truth_table():
    operators = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'XOR': lambda a, b: a != b
    }
    
    values = [True, False]
    
    for op_name, operation in operators.items():
        print(f"Truth table for {op_name}:")
        for a in values:
            for b in values:
                result = operation(a, b)
                print(f"{a} {op_name} {b} = {result}")

if __name__ == '__main__':
    generate_truth_table()