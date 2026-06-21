def is_alphabetic(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def extract_words(text):
    words = []
    current_word = ""
    for char in text:
        if is_alphabetic(char):
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return words

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with 123 numbers and symbols like @#$"
    result = extract_words(sample_string)
    print(result)