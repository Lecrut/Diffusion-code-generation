def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
class TextFormatter:
    def __init__(self, text):
        self.text = text

    def get_formatted_text(self):
        return self.text

if __name__ == '__main__':
    sample_text1 = "this is a test string"
    formatter1 = TextFormatter(sample_text1)
    print("Original:", sample_text1)
    print("Capitalized:", formatter1.get_formatted_text())

    sample_text2 = "another example with different text"
    formatter2 = TextFormatter(sample_text2)
    print("Original:", sample_text2)
    print("Capitalized:", formatter2.get_formatted_text())