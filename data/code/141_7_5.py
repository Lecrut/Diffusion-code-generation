if __name__ == '__main__':
    A = 5
    B = 3
    C = 7
    result_xor = ((A ^ B) ^ (~C))
    result_original = (A & B) | (~C)
    print(f"A: {A}, B: {B}, C: {C}")
    print(f"(A AND B) OR (NOT C) (Original): {result_original}")
    print(f"(A XOR B) XOR (NOT C) (XOR/NOT): {result_xor}")