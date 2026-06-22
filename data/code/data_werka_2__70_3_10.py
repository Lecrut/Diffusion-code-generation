def get_first_and_last(numbers):
    if not numbers:
        raise ValueError("Input list must not be empty")
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    number_list = [int(x) for x in sample_input.split()]
    first, last = get_first_and_last(number_list)
    print(first, last)