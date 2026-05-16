def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    print("Testing AND Gate:")
    a_and = and_gate(True, True)
    print(f"True AND True = {a_and}")
    a_and = and_gate(True, False)
    print(f"True AND False = {a_and}")
    a_and = and_gate(False, True)
    print(f"False AND True = {a_and}")
    a_and = and_gate(False, False)
    print(f"False AND False = {a_and}")
    print("\nTesting OR Gate:")
    a_or = or_gate(True, True)
    print(f"True OR True = {a_or}")
    a_or = or_gate(True, False)
    print(f"True OR False = {a_or}")
    a_or = or_gate(False, True)
    print(f"False OR True = {a_or}")
    a_or = or_gate(False, False)
    print(f"False OR False = {a_or}")
    print("\nTesting NOT Gate:")
    a_not = not_gate(True)
    print(f"NOT True = {a_not}")
    a_not = not_gate(False)
    print(f"NOT False = {a_not}")