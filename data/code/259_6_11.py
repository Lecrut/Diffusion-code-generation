def find_extremes(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    sample_numbers = "34,12,56,78,90"
    result = find_extremes(sample_numbers)
    print(result)