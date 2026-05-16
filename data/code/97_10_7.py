def generate_truth_table(op_name):
    print(f"Truth Table for {op_name}:")
    print("-------------------------")
    a = False
    b = False
    result = False
    print(f"A: {a}, B: {b} -> {op_name}: {result}")
    a = False
    b = True
    if op_name == "AND":
        result = False
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = True
    else:
        result = "Error"
    print(f"A: {a}, B: {b} -> {op_name}: {result}")
    a = True
    b = False
    if op_name == "AND":
        result = False
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = False
    else:
        result = "Error"
    print(f"A: {a}, B: {b} -> {op_name}: {result}")
    a = True
    b = True
    if op_name == "AND":
        result = True
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = False
    else:
        result = "Error"
    print(f"A: {a}, B: {b} -> {op_name}: {result}")
if __name__ == '__main__':
    generate_truth_table("AND")
    print("\n" + "="*30 + "\n")
    generate_truth_table("OR")
    print("\n" + "="*30 + "\n")
    generate_truth_table("NOT_A")