def filter_odd_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 11]
    odd_nums = filter_odd_numbers(sample_values)
    print(odd_nums)