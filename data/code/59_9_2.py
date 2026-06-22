from typing import Union

def sum_digits(number: Union[int, str]) -> int:
    absolute_number = abs(int(number))
    total = 0
    for char in str(absolute_number):
        total += int(char)
    return total

if __name__ == '__main__':
    large_integer = 98765432101234567890
    result = sum_digits(large_integer)
    print(result)