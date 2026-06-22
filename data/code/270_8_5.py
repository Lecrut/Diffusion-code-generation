def remove_spaces(input_string):
    result = []
    for char in input_string:
        if char != " ":
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Remove all spaces from this string"
    processed_string = remove_spaces(sample_input)
    print(processed_string)