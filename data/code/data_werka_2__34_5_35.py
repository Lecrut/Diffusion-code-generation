def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def format_string(input_string):
    return input_string

if __name__ == '__main__':
    SAMPLE_TEXT = "this is a sample string"
    capitalized_text = format_string(SAMPLE_TEXT)
    print("Original:", SAMPLE_TEXT)
    print("Capitalized:", capitalized_text)