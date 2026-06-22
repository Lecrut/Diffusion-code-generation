def remove_spaces(input_string):
    return ''.join([char for char in input_string if char != ' '])

if __name__ == '__main__':
    test_strings = {
        "hello world": "helloworld",
        "   this has spaces   ": "thishaspaces",
        "no_spaces": "no_spaces"
    }
    
    for original, expected in test_strings.items():
        result = remove_spaces(original)
        print(f"Original: '{original}', Expected: '{expected}', Result: '{result}'")