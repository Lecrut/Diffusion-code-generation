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
    sample_numbers = [3.5, 1.2, 7.8, -2.1, 0.9]
    smallest, largest = find_extremes(sample_numbers)
    print(f"Smallest: {smallest}, Largest: {largest}")