def logic_and(a, b):
    return a and b
def logic_or(a, b):
    return a or b
def logic_not(a):
    return not a
def logic_xor(a, b):
    return a ^ b
if __name__ == '__main__':
    x = True
    y = False
    print("--- AND Operation ---")
    print(f"AND({x}, {y}) = {logic_and(x, y)}")
    print("\n--- OR Operation ---")
    print(f"OR({x}, {y}) = {logic_or(x, y)}")
    print("\n--- NOT Operation ---")
    print(f"NOT({x}) = {logic_not(x)}")
    print("\n--- XOR Operation ---")
    print(f"XOR({x}, {y}) = {logic_xor(x, y)}")