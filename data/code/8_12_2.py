import re

def split_by_comma_preserve_quotes(input_string):
    pattern = r'(?:[^",]|"[^"]*")+'
    matches = re.findall(pattern, input_string)
    for i in range(len(matches)):
        token = matches[i]
        if token.startswith('"') and token.endswith('"'):
            matches[i] = token[1:-1]
    return matches

if __name__ == '__main__':
    sample_input = 'hello, "world, of", python, "complex, data, here"'
    result = split_by_comma_preserve_quotes(sample_input)
    print(result)