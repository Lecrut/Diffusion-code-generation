def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 3:
        return sorted_numbers[1]
    else:
        return sum(sorted_numbers) / 3
if __name__ == '__main__':
    sample_list = [5, 2, 8]
    median = find_median(sample_list)
    print(median)