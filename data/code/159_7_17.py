from typing import List

def extract_odd_numbers(numbers: List[int]) -> List[int]:
    odd_nums = []
    for number in numbers:
        if number % 2 != 0:
            odd_nums.append(number)
    return odd_nums

if __name__ == '__main__':
    test_data = [1, 3, 5, 7, 9, 10, 12]
    result = extract_odd_numbers(test_data)
    print(result)