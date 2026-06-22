def find_extremes(numbers):
    if not numbers:
        return None, None
    smallest = largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return smallest, largest

if __name__ == '__main__':
    sample_numbers = [3456789012, 1234567890, 9876543210, 5678901234, 1111111111]
    smallest, largest = find_extremes(sample_numbers)
    print(f"Smallest: {smallest}, Largest: {largest}")