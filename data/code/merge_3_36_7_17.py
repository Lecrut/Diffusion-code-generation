def reverse_string_decorator(func):
    """Decorator that reverses a string upon execution."""
    def wrapper(string):
        return func(string)[::-1] if isinstance(func(string), str) else func(string)
    return wrapper

@reverse_string_decorator
def process_text(text: str) -> str:
    """Process the input text and return it as-is (the decorator handles reversal)."""
    return text.upper()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "12345"
    ]
    
    for sample in samples:
        result = process_text(sample)
        print(f"Original: '{sample}'")
        print(f"Reversed & Processed: '{result}'\n")