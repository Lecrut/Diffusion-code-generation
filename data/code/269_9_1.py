import re
def tokenize_string(text):
    tokens = []
    current_token = ""
    for char in text:
        if re.match(r'\w', char):
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens
if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    result = tokenize_string(sample_string)
    print(result)