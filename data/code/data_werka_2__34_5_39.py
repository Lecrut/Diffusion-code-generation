def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        words = result.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)
    return wrapper

@capitalize_decorator
def get_formatted_text(text):
    return text

if __name__ == '__main__':
    sample_text = "this is a test string"
    formatted_text = get_formatted_text(sample_text)
    print("Original:", sample_text)
    print("Formatted:", formatted_text)