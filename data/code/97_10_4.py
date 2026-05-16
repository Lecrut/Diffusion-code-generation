def generate_truth_table(op_name):
    print(f"Truth Table for {op_name}:")
    print("----------------------")
    A = False
    B = False
    result = False
    print(f"A: {A}, B: {B} -> {op_name}: {result}")
    A = False
    B = True
    if op_name == "AND":
        result = False
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = True
    else:
        result = "Error: Unknown operation"
    print(f"A: {A}, B: {B} -> {op_name}: {result}")
    A = True
    B = False
    if op_name == "AND":
        result = False
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = False
    else:
        result = "Error: Unknown operation"
    print(f"A: {A}, B: {B} -> {op_name}: {result}")
    A = True
    B = True
    if op_name == "AND":
        result = True
    elif op_name == "OR":
        result = True
    elif op_name == "NOT_A":
        result = False
    else:
        result = "Error: Unknown operation"
    print(f"A: {A}, B: {B} -> {op_name}: {result}")
if __name__ == '__main__':
    generate_truth_table("AND")
    print("\n" + "="*20 + "\n")
    generate_truth_table("OR")
    print("\n" + "="*20 + "\n")
    generate_truth_table("NOT_A")