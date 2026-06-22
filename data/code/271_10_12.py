def categorize_characters(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    char_types = {'uppercase': lambda x: x.isupper(), 'lowercase': lambda x: x.islower(), 'digits': lambda x: x.isdigit(), 'special': lambda x: not x.isalnum()}
    categories = {'uppercase': [], 'lowercase': [], 'digits': [], 'special': []}
    for char in text:
        for category, check in char_types.items():
            if check(char):
                categories[category].append(char)
                break
if __name__ == '__main__':
    result = categorize_characters('Hello, World! 123')
    print(result)