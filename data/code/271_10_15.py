class CharacterCategorizer:
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    DIGITS = '0123456789'

    def __init__(self):
        self.categories = {
            'uppercase': [],
            'lowercase': [],
            'digits': [],
            'special': []
        }

    @staticmethod
    def categorize(text):
        categories = {
            'uppercase': [],
            'lowercase': [],
            'digits': [],
            'special': []
        }
        for char in text:
            if char in CharacterCategorizer.UPPERCASE:
                categories['uppercase'].append(char)
            elif char in CharacterCategorizer.LOWERCASE:
                categories['lowercase'].append(char)
            elif char in CharacterCategorizer.DIGITS:
                categories['digits'].append(char)
            else:
                categories['special'].append(char)
        return categories

if __name__ == '__main__':
    categorizer = CharacterCategorizer()
    result = categorizer.categorize("Hello, World! 123")
    print(result)