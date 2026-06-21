import re

def split_string(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    try:
        result = split_string(sample_string)
        print(result)
    except ValueError as e:
        print(e)