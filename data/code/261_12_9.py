def find_median(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(find_median(sample_data))