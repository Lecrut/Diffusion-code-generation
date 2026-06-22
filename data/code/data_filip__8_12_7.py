def split_preserving_quotes(text):
    result = []
    current_token = ""
    in_quotes = False
    for char in text:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(current_token.strip())
            current_token = ""
        else:
            current_token += char
    result.append(current_token.strip())
    return result

if __name__ == '__main__':
    sample_input = 'apple, "banana, split", cherry, "grape, wine", date'
    tokens = split_preserving_quotes(sample_input)
    print(tokens)