def repeat_numbers(input_tuple):
    return [num for num in input_tuple for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    print(repeat_numbers(sample_input))