def extract_alphabetic_words(text):
    words = []
    current_word = ""
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world 123 how are you?"
    result1 = extract_alphabetic_words(sample_string1)
    print(result1)
    sample_string2 = "Python is fun, and learning code is great!"
    result2 = extract_alphabetic_words(sample_string2)
    print(result2)
    sample_string3 = "123!@#$ words with numbers 456."
    result3 = extract_alphabetic_words(sample_string3)
    print(result3)