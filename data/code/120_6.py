import sys
if __name__ == '__main__':
    num1 = 10
    num2 = 10
    result_xor = num1 ^ num2
    is_equal = (num1 ^ num2) == 0
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"XOR result: {result_xor}")
    print(f"Are the XOR results equal to 0 (indicating original numbers were equal)? {is_equal}")