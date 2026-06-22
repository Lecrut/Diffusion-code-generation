def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("The decorated function must return a string.")
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def get_greeting():
    return "hello world"

if __name__ == '__main__':
    sample_text = "this is another test string"
    capitalized_text = get_greeting()
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)