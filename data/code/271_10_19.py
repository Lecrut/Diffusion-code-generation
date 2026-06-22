def categorize_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    char_types = {
        'uppercase': set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        'lowercase': set('abcdefghijklmnopqrstuvwxyz'),
        'digits': set('0123456789')
    }
    
    categories = {
        'uppercase': [],
        'lowercase': [],
        'digits': [],
        'special': []
    }
    
    for char in text:
        if char in char_types['uppercase']:
            categories['uppercase'].append(char)
        elif char in char_types['lowercase']:
            categories['lowercase'].append(char)
        elif char in char_types['digits']:
            categories['digits'].append(char)
        else:
            categories['special'].append(char)
    
    return categories

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = categorize_characters(sample_text)
    print(result)