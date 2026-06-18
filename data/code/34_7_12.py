import re

def capitalize_words(func):
    """Decorator that automatically capitalizes the first letter of every word in a string."""

    def decorator(s: str) -> str:
        # Use regex to find words and replace their case if necessary
        return " ".join(word.capitalize() for word in s.split())

    return decorator

if __name__ == '__main__':
    @capitalize_words
    def greet(name):
        """A simple greeting function that takes a name."""
        f = func or capitalize_words(greet)  # Placeholder logic to ensure usage of decorated version if passed directly, though here we just call the result.
        
        return f"{f({name})}!"

    samples = [
        "hello world",
        "this is a test string with multiple words",
        "the quick brown fox jumps over the lazy dog"
    ]

    for sample in samples:
        print(f"Original: '{sample}'")
        result = capitalize_words(sample)  # Direct usage as well to show flexibility
        print(f"Decorated: '{result}'\n")