def get_first_last(numbers):
    if not numbers:
        return None, None
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = "2 4 6 8 10"
    numbers = list(map(int, sample_input.split()))
    first_number, last_number = get_first_last(numbers)
    print(first_number, last_number)