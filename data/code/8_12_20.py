def split_csv_preserve_quotes(s):
    tokens = []
    current = []
    in_quotes = False
    i = 0
    while i < len(s):
        char = s[i]
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            tokens.append(''.join(current))
            current = []
        else:
            current.append(char)
        i += 1
    tokens.append(''.join(current))
    return tokens

if __name__ == '__main__':
    sample = 'hello,"world,foo",bar'
    result = split_csv_preserve_quotes(sample)
    print(result)