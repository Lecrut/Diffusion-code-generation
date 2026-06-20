def truth_table():
    operations = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'XOR': lambda a, b: a != b
    }
    
    inputs = [True, False]
    
    for op_name, operation in operations.items():
        print(f"\n{op_name} Truth Table:")
        for a in inputs:
            for b in inputs:
                result = operation(a, b)
                print(f"{a} {op_name} {b} = {result}")

if __name__ == '__main__':
    truth_table()