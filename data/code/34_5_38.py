class Capitalizer:
    @staticmethod
    def capitalize_text(text):
        return ' '.join(word.capitalize() for word in text.split())

def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return Capitalizer.capitalize_text(result)
    return wrapper

@capitalize_decorator
def get_greeting():
    return "hello world"

if __name__ == '__main__':
    sample_text = "this is a test string"
    capitalized_text = Capitalizer.capitalize_text(sample_text)
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)