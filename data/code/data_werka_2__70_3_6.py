def get_first_and_last(numbers):
    if not numbers:
        raise ValueError("The sequence of numbers is empty.")
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    numbers = [int(x) for x in sample_input.split()]
    first, last = get_first_and_last(numbers)
    print(first, last)