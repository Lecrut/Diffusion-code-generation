def build_spaced_string(input_list):
    def validate_input(lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        for item in lst:
            if not isinstance(item, (str, int, float)):
                raise ValueError("All elements in the list must be strings, integers, or floats")

    validate_input(input_list)
    
    result = ""
    for i, element in enumerate(input_list):
        result += str(element)
        if i < len(input_list) - 1:
            result += " "
    return result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    output = build_spaced_string(sample_list)
    print(output)