def get_first_last(numbers):
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = "7 14 21 28 35"
    numbers = list(map(int, sample_input.split()))
    first_number, last_number = get_first_last(numbers)
    print(first_number, last_number)