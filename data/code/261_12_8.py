def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 6, 9, 2, 7, 1, 0]
    print(find_median(sample_values))