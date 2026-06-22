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
    sample_values = (15, -3, 88, -42, 99, 1)
    result = find_extremes(sample_values)
    print(f"Smallest value: {result[0]}")
    print(f"Largest value: {result[1]}")