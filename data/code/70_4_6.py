def get_first_last(numbers):
    if numbers:
        return numbers[0], numbers[-1]
    else:
        return None, None

if __name__ == '__main__':
    sample_input = "2 4 6 8 10"
    numbers = list(map(int, sample_input.split()))
    first_number, last_number = get_first_last(numbers)
    print(first_number, last_number)