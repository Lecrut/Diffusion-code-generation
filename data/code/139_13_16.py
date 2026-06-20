def and_gate(A: bool, B: bool) -> bool:
    return A & B

def or_gate(A: bool, B: bool) -> bool:
    return A | B

def not_gate(A: bool) -> bool:
    return not A

if __name__ == '__main__':
    print(f"AND(True, True): {and_gate(True, True)}")
    print(f"AND(True, False): {and_gate(True, False)}")
    print(f"OR(True, False): {or_gate(True, False)}")
    print(f"OR(False, False): {or_gate(False, False)}")
    print(f"NOT(True): {not_gate(True)}")
    print(f"NOT(False): {not_gate(False)}")