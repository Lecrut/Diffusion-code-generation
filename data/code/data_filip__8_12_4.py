import re

def split_preserving_quotes(text):
    pattern = r'[^,\s"]+|"([^"]*)"'
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        if match:
            result.append(match)
        else:
            split_part = match[0]
            result.append(split_part)
    return result

def split_complex_string(text):
    pattern = r'"([^"]*)"|([^,]+)'
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        if match[0]:
            result.append(match[0])
        elif match[1]:
            result.append(match[1])
    return result

if __name__ == '__main__':
    test_input = 'apple, "banana, cherry", date, "fig, grape", kiwi'
    tokens = split_complex_string(test_input)
    print(tokens)