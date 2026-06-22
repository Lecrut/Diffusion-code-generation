def process_sequence(numbers):
    if not numbers:
        raise ValueError("Input sequence cannot be empty")
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    number_list = [int(x) for x in sample_input.split()]
    first, last = process_sequence(number_list)
    print(first)
    print(last)