import sys
def multiply_large_integers(num1_str: str, num2_str: str) -> int:
    if not num1_str or not num2_str:
        return 0
    a = int(num1_str)
    b = int(num2_str)
    result = a * b
    return result
if __name__ == '__main__':
    sample_num1 = "9007199254740993"                                                     
    sample_num2 = "8007199254740993"
    result_value = multiply_large_integers(sample_num1, sample_num2)
    print(result_value)