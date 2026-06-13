import re
def split_string_basic(text):
    return text.split(' ')
def split_string_regex(text):
    return re.findall(r'\S+|\s+', text)
if __name__ == '__main__':
    sample_string = "This   has  multiple   spaces"
    result_basic = split_string_basic(sample_string)
    result_regex = split_string_regex(sample_string)
    print("Original String:", sample_string)
    print("Basic Split Result:", result_basic)
    print("Regex Split Result:", result_regex)