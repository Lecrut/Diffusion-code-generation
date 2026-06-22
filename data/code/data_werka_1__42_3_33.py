def build_spaced_string(input_list):
    def validate_input(lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
    
    validate_input(input_list)
    
    result = ""
    for i, element in enumerate(input_list):
        result += str(element)
        if i < len(input_list) - 1:
            result += " "
    return result

if __name__ == '__main__':
    sample_list = ["hello", "world", "this", "is", "a", "test"]
    output_string = build_spaced_string(sample_list)
    print(output_string)