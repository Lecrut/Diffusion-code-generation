import re
def tokenize_with_punctuation_separation(text):
    tokens = []
    for char in text:
        if char.isalnum():
            if tokens and tokens[-1] == ' ':
                tokens.append(char)
            else:
                tokens.append(char)
        elif char in '.,!?;:':
            if tokens and tokens[-1] != ' ':
                tokens.append(char)
            elif not tokens or tokens[-1] == ' ':
                tokens.append(char)
        else:
            if tokens and tokens[-1] != ' ':
                tokens.append(char)
    return tokens
if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    result = tokenize_with_punctuation_separation(sample_string)
    print(result)