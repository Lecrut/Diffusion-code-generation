import re

def capitalize_words(text: str) -> str:
    """Return a new string with the first letter of each word capitalized."""
    return ' '.join(word.capitalize() if len(word.strip()) > 0 else '' 
                   for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world, this is my example"
    result = capitalize_words(sample_text)
    print(result)