import sys
if __name__ == '__main__':
    num1 = 10
    num2 = 10
    result_xor = num1 ^ num2
    is_equal_xor = (result_xor == 0)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"XOR result: {result_xor}")
    print(f"Are the XOR results equal (i.e., is the XOR result 0)? {is_equal_xor}")