import re
def tokenize_string(text):
    tokens = []
    for match in re.finditer(r"(\w+)([^a-zA-Z0-9]*)|([^a-zA-Z0-9]+)", text):
        if match.group(1):
            tokens.append(match.group(1))
        elif match.group(2) or match.group(3):
            tokens.append(match.group(2) or match.group(3))
    return tokens
if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    result = tokenize_string(sample_string)
    print(result)