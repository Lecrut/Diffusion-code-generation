class TextFormatter:
    def capitalize(self, text):
        return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    formatter = TextFormatter()
    sample_text = "a journey into the world of programming"
    capitalized_text = formatter.capitalize(sample_text)
    print(capitalized_text)