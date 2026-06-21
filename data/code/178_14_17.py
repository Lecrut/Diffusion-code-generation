import re

def split_string(text):
    words = [word for word in re.findall(r'\S+', text) if word]
    return words

if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    result = split_string(sample_string)
    print(result)