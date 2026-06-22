def find_extremes(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    smallest = largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number

    return (smallest, largest)

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 1, 5, 6]
    print(find_extremes(sample_numbers))