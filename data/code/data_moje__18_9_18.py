def median_via_integer_division(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        lower = sorted_numbers[(n - 1) // 2]
        upper = sorted_numbers[n // 2]
        return (lower + upper) // 2

if __name__ == '__main__':
    sample_lists = [
        [3, 1, 2, 4, 5],
        [10, 20, 30, 40],
        [5],
        [7, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for sample in sample_lists:
        print(median_via_integer_division(sample))