def build_spaced_string(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    
    result = []
    for element in input_list:
        if not isinstance(element, str):
            raise ValueError("All elements in the list must be strings.")
        result.append(str(element))
    
    return " ".join(result)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        output = build_spaced_string(sample_list)
        print(output)
    except ValueError as e:
        print(e)