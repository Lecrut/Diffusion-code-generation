def find_extremes(numbers):
    if not numbers:
        return None, None
    smallest = largest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return smallest, largest

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 1.618, 0.577, 1.414]
    smallest, largest = find_extremes(sample_numbers)
    print(f"Smallest: {smallest}, Largest: {largest}")