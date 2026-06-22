import re

def find_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text.lower())
    return sorted(list(set(words)))

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test String with numbers 123 and symbols @#$."
    result = find_words(sample_text)
    print(result)