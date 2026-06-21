class WordCapitalizer:
    def __init__(self, text):
        self.text = text

    def capitalize(self):
        return ' '.join(word.capitalize() for word in self.text.split())

if __name__ == '__main__':
    sample_text = "welcome to the world of ai"
    capitalizer = WordCapitalizer(sample_text)
    capitalized_text = capitalizer.capitalize()
    print(capitalized_text)