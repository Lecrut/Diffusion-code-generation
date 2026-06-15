import re
def tokenize_with_punctuation(text):
    tokens = []
    current_word = ""
    for char in text:
        if re.match(r'\w', char):
            current_word += char
        else:
            if current_word:
                tokens.append(current_word)
                current_word = ""
            tokens.append(char)
    if current_word:
        tokens.append(current_word)
    return tokens
if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    result = tokenize_with_punctuation(sample_string)
    print(result)