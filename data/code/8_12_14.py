def split_csv_string(input_string):
    tokens = []
    current_token = []
    in_quotes = False
    i = 0
    length = len(input_string)
    
    while i < length:
        char = input_string[i]
        
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            tokens.append(''.join(current_token))
            current_token = []
        else:
            current_token.append(char)
        i += 1
        
    tokens.append(''.join(current_token))
    
    return [token.strip() for token in tokens]

if __name__ == '__main__':
    test_input = 'hello,"world, foo",bar,"baz"'
    result = split_csv_string(test_input)
    print(result)