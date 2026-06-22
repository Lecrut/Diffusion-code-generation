def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

class TextProcessor:
    @staticmethod
    def process(text):
        return text

@capitalize_decorator
def get_greeting():
    return "hello world"

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "this is a test string"
    processed_text = processor.process(sample_text)
    capitalized_text = get_greeting()
    print("Original:", sample_text)
    print("Processed:", processed_text)
    print("Capitalized Greeting:", capitalized_text)