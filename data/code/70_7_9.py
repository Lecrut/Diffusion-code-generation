def process_string(input_string):
    words = input_string.split()
    if words:
        return words[0], words[-1]
    else:
        return None, None

if __name__ == '__main__':
    sample_string = "Hello world this is a test string"
    first_word, last_word = process_string(sample_string)
    print(first_word, last_word)