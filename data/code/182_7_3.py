def separate_characters(input_string):
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char
    return result
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    separated = separate_characters(sample_string)
    print(separated)