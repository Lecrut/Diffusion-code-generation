from functools import reduce
def remove_even_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if not (num % 2 == 0)]
def filter_strings_by_length(strings: list[str], min_len: int) -> list[str]:
    return [s for s in strings if len(s) >= min_len]
if __name__ == '__main__':
    sample_numbers = [1, 4, 5, 8, 9, 20]
    filtered_nums = remove_even_numbers(sample_numbers)
    sample_strings = ["apple", "banana", "kiwi", "grape"]
    filtered_strs = filter_strings_by_length(sample_strings, min_len=3)
    print("Filtered numbers:", filtered_nums)
    print("Filtered strings:", filtered_strs)