def categorize_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    categories = {
        'uppercase': [],
        'lowercase': [],
        'digits': [],
        'special': []
    }
    
    for char in text:
        if char.isupper():
            categories['uppercase'].append(char)
        elif char.islower():
            categories['lowercase'].append(char)
        elif char.isdigit():
            categories['digits'].append(char)
        else:
            categories['special'].append(char)
    
    return categories

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = categorize_characters(sample_text)
    print(result)