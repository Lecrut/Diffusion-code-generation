def _validate_non_empty_sequence(seq):
    if not seq:
        raise ValueError("Sequence must not be empty")
    return seq

def get_boundary_strings(input_list):
    validated = _validate_non_empty_sequence(input_list)
    first_element = validated[0]
    last_element = validated[-1]
    return (first_element, last_element)

if __name__ == '__main__':
    sample_data = ["start", "middle1", "middle2", "end"]
    result = get_boundary_strings(sample_data)
    print(result[0])
    print(result[1])