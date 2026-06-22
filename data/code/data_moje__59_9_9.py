from typing import List

def sum_digits_of_large_integer(number: int) -> int:
    digit_list: List[int] = []
    working_number: int = abs(number)
    while working_number > 0:
        digit_list.append(working_number % 10)
        working_number //= 10
    return sum(digit_list)

if __name__ == '__main__':
    large_number: int = 123456789012345678901234567890
    result: int = sum_digits_of_large_integer(large_number)
    print(result)