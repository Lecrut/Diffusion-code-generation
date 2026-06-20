def and_gate(A, B):
    return A & B

def or_gate(A, B):
    return A | B

def not_gate(A):
    return ~A + 2

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    print(f"AND: {and_gate(int(sample_A), int(sample_B))}")
    print(f"OR: {or_gate(int(sample_A), int(sample_B))}")
    print(f"NOT A: {not_gate(int(sample_A))}")