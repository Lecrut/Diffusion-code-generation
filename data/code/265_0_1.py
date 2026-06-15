def extract_alphabetic(input_string):
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            result += char
    return result
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    extracted_chars = extract_alphabetic(sample_string)
    print(extracted_chars)