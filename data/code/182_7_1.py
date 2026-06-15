def separate_characters(input_string):
    characters = []
    for char in input_string:
        if char.isalpha():
            characters.append(char)
    return "".join(characters)
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    result = separate_characters(sample_string)
    print(result)