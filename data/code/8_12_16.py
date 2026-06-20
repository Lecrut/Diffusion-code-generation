import re

def split_by_commas_preserve_quotes(s):
    tokens = []
    current_token = []
    in_quotes = False
    i = 0
    while i < len(s):
        char = s[i]
        if char == '"':
            in_quotes = not in_quotes
            i += 1
        elif char == ',' and not in_quotes:
            tokens.append(''.join(current_token).strip())
            current_token = []
            i += 1
        else:
            current_token.append(char)
            i += 1
    tokens.append(''.join(current_token).strip())
    return tokens

if __name__ == '__main__':
    sample = 'hello, "world, foo", bar, "baz, qux"'
    result = split_by_commas_preserve_quotes(sample)
    print(result)