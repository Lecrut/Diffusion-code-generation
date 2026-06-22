def sort_and_print(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    sample_list = [10, 25, 33, 47, 51]
    sort_and_print(sample_list)