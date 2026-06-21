def is_odd(number: int) -> bool:
    return number % 2 != 0

def filter_odd_numbers(numbers: list[int]) -> list[int]:
    odd_numbers = []
    for number in numbers:
        if is_odd(number):
            odd_numbers.append(number)
    return odd_numbers

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(sample_list)
    print(result)