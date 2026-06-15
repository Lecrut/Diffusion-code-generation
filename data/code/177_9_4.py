import re
def split_string_by_whitespace(text):
    return re.split(r'\s+', text)
if __name__ == '__main__':
    sample1 = "Hello world"
    print(f"'{sample1}' split: {split_string_by_whitespace(sample1)}")
    sample2 = "  This   has\tmultiple\nspaces "
    print(f"'{sample2}' split: {split_string_by_whitespace(sample2)}")
    sample3 = "NoSpacesHere"
    print(f"'{sample3}' split: {split_string_by_whitespace(sample3)}")
    sample4 = "a\t\nb\r\n c"
    print(f"'{sample4}' split: {split_string_by_whitespace(sample4)}")