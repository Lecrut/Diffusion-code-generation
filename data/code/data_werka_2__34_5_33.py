def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def format_text(text):
    return text

if __name__ == '__main__':
    sample_text = "this is a test string"
    capitalized_text = format_text(sample_text)
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)