def get_first_and_last(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    first, last = get_first_and_last(sample_numbers)
    print(first, last)