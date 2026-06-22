class CharacterCategorizer:
    def __init__(self):
        self.categories = {
            'uppercase': [],
            'lowercase': [],
            'digits': [],
            'special': []
        }

    def categorize(self, text):
        for char in text:
            if char.isupper():
                self.categories['uppercase'].append(char)
            elif char.islower():
                self.categories['lowercase'].append(char)
            elif char.isdigit():
                self.categories['digits'].append(char)
            else:
                self.categories['special'].append(char)

if __name__ == '__main__':
    categorizer = CharacterCategorizer()
    sample_text = "Hello, World! 123"
    categorizer.categorize(sample_text)
    print(categorizer.categories)