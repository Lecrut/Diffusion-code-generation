import sys
def xor_operation(a, b):
    return a ^ b
if __name__ == '__main__':
    input_a = 10
    input_b = 5
    result = xor_operation(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"XOR Result: {result}")