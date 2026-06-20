def get_first_last(numbers):
    if numbers:
        return numbers[0], numbers[-1]
    else:
        return None, None

if __name__ == '__main__':
    sample_input = "25 35 45 55"
    number_list = list(map(int, sample_input.split()))
    first_number, last_number = get_first_last(number_list)
    print(first_number, last_number)