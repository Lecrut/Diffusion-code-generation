def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 76]
    find_min_max(sample_numbers)