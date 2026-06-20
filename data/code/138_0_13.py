def generate_truth_table():
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'XOR': lambda x, y: x != y
    }
    
    for op_name, operation in operations.items():
        print(f"Truth table for {op_name}:")
        for x in [True, False]:
            for y in [True, False]:
                result = operation(x, y)
                print(f"{x} {op_name} {y} = {result}")

if __name__ == '__main__':
    generate_truth_table()