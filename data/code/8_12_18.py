import re

def split_by_commas_preserving_quotes(s):
    if not s:
        return []
    
    tokens = []
    current_token = []
    in_quotes = False
    quote_char = None
    i = 0
    
    while i < len(s):
        char = s[i]
        
        if in_quotes:
            current_token.append(char)
            if char == quote_char:
                in_quotes = False
                quote_char = None
        else:
            if char in ('"', "'"):
                in_quotes = True
                quote_char = char
                current_token.append(char)
            elif char == ',':
                tokens.append(''.join(current_token).strip())
                current_token = []
            else:
                current_token.append(char)
        
        i += 1
    
    if current_token or s and s[-1] == ',':
        tokens.append(''.join(current_token).strip())
    
    return tokens

if __name__ == '__main__':
    test_string = 'apple,"banana, berry",cherry,"date, elderberry",fig'
    result = split_by_commas_preserving_quotes(test_string)
    print(result)