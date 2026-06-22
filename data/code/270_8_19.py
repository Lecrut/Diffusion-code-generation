def remove_spaces(input_string):
    result = ""
    for char in input_string:
        if char != " ":
            result += char
    return result

if __name__ == '__main__':
    sample_input = "Example string with spaces"
    print(remove_spaces(sample_input))