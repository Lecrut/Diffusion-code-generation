if __name__ == '__main__':
    A = 10
    B = 5
    C = 3
    result_xor = ((A ^ B) ^ (~C))
    result_and_or_not = (A & B) | (~C)
    print(f"A = {A}, B = {B}, C = {C}")
    print(f"(A AND B) OR (NOT C) = {result_and_or_not}")
    print(f"XOR/NOT equivalent = {result_xor}")