def find_lowest_number(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    try:
        print(f"Smallest in {sample_numbers}: {find_lowest_number(sample_numbers)}")
    except ValueError as e:
        print(e)