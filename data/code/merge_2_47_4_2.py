import sys
def multiply_large_integers(num1_str: str, num2_str: str) -> int:
    if not num1_str.isdigit() and '.' in num1_str:
        raise ValueError("Input must be a non-negative integer.")
    result = 0
    def convert_to_integer(string_number):
        return int(string_number.replace('.', '').lstrip('-'))
    big_num_1 = convert_to_integer(num1_str)
    big_num_2 = convert_to_integer(num2_str)
    if not (big_num_1 > -sys.maxsize and big_num_2 > -sys.maxsize):
        raise ValueError("Inputs must be within integer limits.")
    result = int(big_num_1 * big_num_2)
    return result
if __name__ == '__main__':
    num_a = "9007199254740993"
    num_b = "8675309000000000"
    final_result = multiply_large_integers(num_a, num_b)
    print(final_result)