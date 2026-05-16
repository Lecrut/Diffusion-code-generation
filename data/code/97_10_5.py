def generate_truth_table(op_name):
    print(f"Truth Table for {op_name}:")
    print("--------------------------")
    print(f"{'A':<5} | {'B':<5} | {op_name}:")
    print("-----|-----|----------")
    a = False
    b = False
    result = False
    print(f"{str(a):<5} | {str(b):<5} | {op_name}: {str(result)}")
    a = False
    b = True
    result = False
    print(f"{str(a):<5} | {str(b):<5} | {op_name}: {str(result)}")
    a = True
    b = False
    result = False
    print(f"{str(a):<5} | {str(b):<5} | {op_name}: {str(result)}")
    a = True
    b = True
    result = True
    print(f"{str(a):<5} | {str(b):<5} | {op_name}: {str(result)}")
if __name__ == '__main__':
    generate_truth_table("AND")