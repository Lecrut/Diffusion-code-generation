import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

if __name__ == '__main__':
    sample_strings = {
        "sample_string1": "This is a sample sentence for testing.",
        "sample_string2": "  Multiple   spaces   between words here. ",
        "sample_string3": "",
        "sample_string4": "OneWord",
        "sample_string5": "Hello, world! How are you?"
    }
    
    for key, value in sample_strings.items():
        print(f"'{value}': {count_words(value)}")