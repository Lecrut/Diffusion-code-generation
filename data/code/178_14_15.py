import re

def split_string_clean(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    result_clean = split_string_clean(sample_string)
    print(result_clean)