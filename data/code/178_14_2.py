import re
def split_string_basic(text):
    return text.split(' ')
def split_string_regex(text):
    return re.findall(r'\S+|\s+', text)
if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    result_basic = split_string_basic(sample_string)
    result_regex = split_string_regex(sample_string)
    print("Original String:", repr(sample_string))
    print("Basic Split Result:", result_basic)
    print("Regex Split Result:", result_regex)