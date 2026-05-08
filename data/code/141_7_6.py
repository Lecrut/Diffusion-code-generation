if __name__ == '__main__':
    A = 5
    B = 3
    C = 7
    result_xor = ((A ^ B) ^ (~C))
    result_and_or = (A & B) | (~C)
    print(f"A = {A}, B = {B}, C = {C}")
    print(f"(A AND B) OR (NOT C) = {result_and_or}")
    print(f"XOR/NOT implementation = {result_xor}")