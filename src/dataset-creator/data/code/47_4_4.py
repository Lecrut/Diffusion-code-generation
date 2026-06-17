import sys
def multiply_large_integers(num1: int, num2: int) -> int:
    return num1 * num2
if __name__ == '__main__':
    sample_value_1 = 9007199254740993
    sample_value_2 = 8675309000000000
    result = multiply_large_integers(sample_value_1, sample_value_2)
    print(result)