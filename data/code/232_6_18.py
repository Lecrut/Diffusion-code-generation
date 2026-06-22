def generate_growing_sequence(initial_value, length):
    if not isinstance(initial_value, int) or initial_value < 100:
        raise ValueError("Initial value must be an integer greater than or equal to 100.")
    
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    return list(map(lambda x: initial_value + x * (initial_value - 100), range(length)))

if __name__ == '__main__':
    initial_value = 100
    length = 15
    sequence = generate_growing_sequence(initial_value, length)
    print(sequence)