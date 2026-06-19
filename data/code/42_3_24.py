def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    for element in input_list:
        if not isinstance(element, (str, int, float)):
            raise ValueError("All elements in the list must be strings, integers, or floats.")

def build_spaced_string(input_list):
    validate_input(input_list)
    result = []
    for element in input_list:
        result.append(str(element))
    return " ".join(result)

if __name__ == '__main__':
    sample_list = ["apple", 42, "cherry", 3.14]
    output_string = build_spaced_string(sample_list)
    print(output_string)