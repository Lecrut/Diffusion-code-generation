def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        capitalized_result = ' '.join(word.capitalize() for word in result.split())
        return capitalized_result
    return wrapper

@capitalize_decorator
def get_greeting():
    return "hello world"

if __name__ == '__main__':
    sample_text = "this is a test string"
    capitalized_text = get_greeting()
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)