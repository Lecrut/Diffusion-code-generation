def compare_adjacent_characters(input_string):
    if not isinstance(input_string, str) or len(input_string) < 2:
        raise ValueError("Input must be a string of at least two characters.")
    
    result = []
    for i in range(len(input_string) - 1):
        if input_string[i] < input_string[i+1]:
            result.append('ascending')
        elif input_string[i] > input_string[i+1]:
            result.append('descending')
        else:
            result.append('equal')
    
    return result

if __name__ == '__main__':
    sample_input = "abcde"
    try:
        output = compare_adjacent_characters(sample_input)
        print(output)
    except ValueError as e:
        print(e)