def subtract_sequence(start_number, sequence):
    for number in sequence:
        yield start_number - number
if __name__ == '__main__':
    fixed_start = 100
    input_sequence = [10, 25, 50, 75]
    result_generator = subtract_sequence(fixed_start, input_sequence)
    results = list(result_generator)
    print(results)