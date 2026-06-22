UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'

def categorize_characters(text):
    categories = {
        'uppercase': [],
        'lowercase': [],
        'digits': [],
        'special': []
    }
    for char in text:
        if char in UPPERCASE:
            categories['uppercase'].append(char)
        elif char in LOWERCASE:
            categories['lowercase'].append(char)
        elif char in DIGITS:
            categories['digits'].append(char)
        else:
            categories['special'].append(char)
    return categories

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    categorized = categorize_characters(sample_text)
    print(categorized)