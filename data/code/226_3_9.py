REPEAT_COUNT = 5

def flatten_sequence(input_tuple):
    return [num for num in input_tuple for _ in range(REPEAT_COUNT)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    print(flatten_sequence(sample_input))