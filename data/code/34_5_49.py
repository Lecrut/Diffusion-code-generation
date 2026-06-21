def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def get_greeting():
    return "hello world"

@capitalize_decorator
def format_text(text):
    return text

if __name__ == '__main__':
    sample_texts = {
        "sample1": "this is a test string",
        "sample2": "another example with multiple words"
    }
    
    for key, value in sample_texts.items():
        original_text = value
        capitalized_text = format_text(value)
        print(f"Original ({key}):", original_text)
        print(f"Capitalized ({key}):", capitalized_text)