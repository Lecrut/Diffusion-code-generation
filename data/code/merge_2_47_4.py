import sys
def multiply_large_integers(num1: int, num2: int) -> int:
    return num1 * num2
if __name__ == '__main__':
    sample_num1 = 9007199254740993
    sample_num2 = 8007199254740993
    result = multiply_large_integers(sample_num1, sample_num2)
    print(result)