def extract_first_word(input_string):
    words = input_string.split()
    if words:
        return words[0]
    else:
        return ""
if __name__ == '__main__':
    sample_input = "This is a sample string to test the function"
    result = extract_first_word(sample_input)
    print(result)