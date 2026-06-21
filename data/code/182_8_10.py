CHAR_SEPARATOR = " - "

def separate_string(input_string):
    separated_chars = []
    for index, char in enumerate(input_string):
        separated_chars.append(f"{index}{CHAR_SEPARATOR}{char}")
    return separated_chars

if __name__ == '__main__':
    sample_string = "Hello World"
    result = separate_string(sample_string)
    print("Separated characters with indices:", result)