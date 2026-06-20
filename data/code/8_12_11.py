def split_preserving_quotes(text: str) -> list:
    result = []
    current_token = []
    in_quotes = False
    quote_char = None
    i = 0
    length = len(text)
    
    while i < length:
        char = text[i]
        
        if not in_quotes:
            if char == '"':
                in_quotes = True
                quote_char = '"'
                current_token.append(char)
            elif char == "'":
                in_quotes = True
                quote_char = "'"
                current_token.append(char)
            elif char == ',':
                if current_token:
                    token_str = ''.join(current_token).strip()
                    if token_str.startswith(('"', "'")) and token_str.endswith(('"', "'")):
                        token_str = token_str[1:-1]
                    result.append(token_str)
                current_token = []
            else:
                current_token.append(char)
        else:
            if char == quote_char:
                in_quotes = False
                quote_char = None
                current_token.append(char)
            else:
                current_token.append(char)
        i += 1
    
    if current_token:
        token_str = ''.join(current_token).strip()
        if token_str.startswith(('"', "'")) and token_str.endswith(('"', "'")):
            token_str = token_str[1:-1]
        if token_str:
            result.append(token_str)
            
    return result

if __name__ == '__main__':
    sample_input = 'John, "Alice, Bob", 42, "Charlie" , "Eve, Frank"'
    tokens = split_preserving_quotes(sample_input)
    print(tokens)