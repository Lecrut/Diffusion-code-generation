def get_even_numbers(start, end):
    return [num for num in range(start, end + 1) if num % 2 == 0]

if __name__ == '__main__':
    sample_start = 5
    sample_end = 30
    even_numbers = get_even_numbers(sample_start, sample_end)
    print(even_numbers)