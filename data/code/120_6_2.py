import sys
if __name__ == '__main__':
    num1 = 10
    num2 = 10
    result_xor = num1 ^ num2
    if result_xor == 0:
        print("The XOR result is 0, meaning the original numbers are equal.")
    else:
        print("The XOR result is not 0, meaning the original numbers are not equal.")