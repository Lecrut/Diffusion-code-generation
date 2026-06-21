BORDER_FIRST = 0
BORDER_LAST = -1

def get_boundary_elements(input_sequence):
    if len(input_sequence) == 0:
        raise ValueError("Sequence must contain at least one element")
    first_element = input_sequence[BORDER_FIRST]
    last_element = input_sequence[BORDER_LAST]
    return (first_element, last_element)

if __name__ == '__main__':
    raw_input_data = "5 12 8 19 3"
    numeric_sequence = list(map(int, raw_input_data.split()))
    boundary_values = get_boundary_elements(numeric_sequence)
    print(boundary_values)