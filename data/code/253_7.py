def find_median(numbers):
    if len(numbers) != 3:
        raise ValueError("Input list must contain exactly three numbers.")
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[1]
    return median
if __name__ == '__main__':
    sample_list = [5, 2, 8]
    result = find_median(sample_list)
    print(result)