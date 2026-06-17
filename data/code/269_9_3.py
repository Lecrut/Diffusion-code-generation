import re
def tokenize_with_punctuation_separation(text):
    tokens = []
    for char in text:
        if char.isalnum():
            tokens.append(char)
        elif not char.isspace() and not char.isspace():
            tokens.append(char)
        else:
            if tokens and (tokens[-1].isalnum()):
                tokens.append(char)
            elif not tokens or not tokens[-1].isalnum():
                tokens.append(char)
    return tokens
if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    result = tokenize_with_punctuation_separation(sample_string)
    print(result)