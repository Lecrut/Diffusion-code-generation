def split_csv(csv_string):
    result = []
    current = []
    in_quotes = False
    escape_next = False

    for char in csv_string:
        if escape_next:
            current.append(char)
            escape_next = False
        elif char == '\\' and in_quotes:
            escape_next = True
        elif char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            segment = ''.join(current)
            if segment:
                result.append(segment)
            current = []
        else:
            current.append(char)

    segment = ''.join(current)
    if segment:
        result.append(segment)

    return result

if __name__ == '__main__':
    samples = [
        'a,b,c',
        'a,,b',
        'a,"b,c",d',
        'a,"b""c",d',
        ',,',
        'a,b,c,',
        ',a,b,c',
        'hello world',
        '',
        '"hello",world',
        'a,\t,b',
    ]
    for sample in samples:
        print(split_csv(sample))