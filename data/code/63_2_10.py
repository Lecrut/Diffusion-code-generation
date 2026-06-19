FIRST_ELEMENT_INDEX = 0

def fetch_initial_value(numbers):
    return numbers[FIRST_ELEMENT_INDEX]

if __name__ == '__main__':
    example_sequence = [9, 18, 27, 36]
    print(fetch_initial_value(example_sequence))