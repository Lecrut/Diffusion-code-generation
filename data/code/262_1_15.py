def find_extremes(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, 2.9, 0.7]
    result = find_extremes(sample_numbers)
    print(f"Smallest: {result[0]}, Largest: {result[1]}")