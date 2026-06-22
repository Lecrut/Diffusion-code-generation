class CharacterCategorizer:
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    DIGITS = '0123456789'

    def categorize(self, text):
        categories = {
            'uppercase': [],
            'lowercase': [],
            'digits': [],
            'special': []
        }
        for char in text:
            if char in self.UPPER:
                categories['uppercase'].append(char)
            elif char in self.LOWER:
                categories['lowercase'].append(char)
            elif char in self.DIGITS:
                categories['digits'].append(char)
            else:
                categories['special'].append(char)
        return categories

if __name__ == '__main__':
    categorizer = CharacterCategorizer()
    result = categorizer.categorize("Hello, World! 123")
    print(result)