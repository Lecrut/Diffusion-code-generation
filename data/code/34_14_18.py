import re

def capitalize_words(text: str) -> str:
    """Capitalizes the first letter of each word in the string."""
    return ' '.join(word.capitalize() if word else '' 
                   for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world, this is a test."
    result = capitalize_words(sample_text)
    print(result)