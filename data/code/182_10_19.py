def separate_characters(input_string, delimiter):
    if not isinstance(input_string, str) or not isinstance(delimiter, str):
        raise ValueError("Both input_string and delimiter must be strings.")
    
    return delimiter.join(char for char in input_string)

if __name__ == '__main__':
    result = separate_characters("hello", ", ")
    print(result)