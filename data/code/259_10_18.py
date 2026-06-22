def find_extremes(numbers):
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    result = find_extremes(sample_list)
    print(f"Smallest value: {result[0]}")
    print(f"Largest value: {result[1]}")