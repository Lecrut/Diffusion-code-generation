import re

def split_phrase(text):
    return [word for word in re.findall(r'\b\w+\b', text.strip()) if word]

if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    result = split_phrase(sample_string)
    print(result)