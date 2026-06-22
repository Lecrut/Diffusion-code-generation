def find_extremes(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return smallest, largest

if __name__ == '__main__':
    sample_values = (15, -3, 88, -42, 99, 1)
    extremes = find_extremes(sample_values)
    print(f"Input values: {sample_values}")
    print(f"Smallest value: {extremes[0]}")
    print(f"Largest value: {extremes[1]}")