def get_boundary_elements(sequence):
    if len(sequence) < 1:
        raise ValueError("Sequence must contain at least one number")
    return sequence[0], sequence[-1]

def parse_input_string(raw_input):
    if not raw_input:
        raise ValueError("Input string cannot be empty")
    tokens = raw_input.strip().split()
    return [int(token) for token in tokens]

if __name__ == '__main__':
    raw_data = "5 15 25 35 45"
    numbers = parse_input_string(raw_data)
    first_val, last_val = get_boundary_elements(numbers)
    print(first_val, last_val)