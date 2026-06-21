def identify_odd_numbers(start, end):
    return [num for num in range(start, end + 1) if num % 2 != 0]

if __name__ == '__main__':
    sample_start = 1
    sample_end = 50
    odd_numbers = identify_odd_numbers(sample_start, sample_end)
    print(odd_numbers)