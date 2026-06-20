import re

def split_preserving_quotes(text):
    pattern = re.compile(r'([",]|"[^"]*"|[^,]+)')
    tokens = pattern.findall(text)
    result = []
    buffer = []
    in_quotes = False
    for char in text:
        if char == '"':
            in_quotes = not in_quotes
            buffer.append(char)
        elif char == ',' and not in_quotes:
            token = "".join(buffer).strip()
            if token:
                result.append(token)
            buffer = []
        else:
            buffer.append(char)
    token = "".join(buffer).strip()
    if token:
        result.append(token)
    return result

if __name__ == '__main__':
    sample_input = 'apple, "banana, split", cherry, "date, fig"'
    tokens = split_preserving_quotes(sample_input)
    print(tokens)