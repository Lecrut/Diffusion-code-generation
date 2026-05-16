def logical_and(a, b):
    return a and b
def logical_or(a, b):
    return a or b
def logical_not(a):
    return not a
def logical_xor(a, b):
    return a ^ b
if __name__ == '__main__':
    val1 = True
    val2 = False
    print("--- Logical AND ---")
    print(f"AND({val1}, {val2}) = {logical_and(val1, val2)}")
    print("\n--- Logical OR ---")
    print(f"OR({val1}, {val2}) = {logical_or(val1, val2)}")
    print("\n--- Logical NOT ---")
    print(f"NOT({val1}) = {logical_not(val1)}")
    print("\n--- Logical XOR ---")
    print(f"XOR({val1}, {val2}) = {logical_xor(val1, val2)}")