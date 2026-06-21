def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        words = result.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)
    return wrapper

@capitalize_decorator
def format_text(text):
    return text

if __name__ == '__main__':
    sample_text = "another example with different words"
    capitalized_text = format_text(sample_text)
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)