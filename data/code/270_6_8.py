def remove_spaces(input_string):
    return ''.join([char for char in input_string if char != ' '])

if __name__ == '__main__':
    test_strings = {
        "hello world": "helloworld",
        "   this has spaces   ": "thishaspaces",
        "no_spaces": "nospaces"
    }
    
    results = {test_string: remove_spaces(test_string) for test_string in test_strings}
    
    for input_string, result in results.items():
        print(f'Input: "{input_string}" | Output: "{result}"')