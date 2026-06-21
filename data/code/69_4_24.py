def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if len(input_list) < 2:
        raise ValueError("List must contain at least two elements")

def extract_every_second_element(input_list):
    validate_input(input_list)
    return [input_list[i] for i in range(0, len(input_list), 2)]

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z', 'w', 'v', 'u']
    result = extract_every_second_element(sample_list)
    print(result)