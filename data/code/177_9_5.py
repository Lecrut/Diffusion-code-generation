import re
def split_string_by_whitespace(text):
    return re.split(r'\s+', text)
if __name__ == '__main__':
    sample1 = "Hello world"
    sample2 = "  This   has\tmultiple\nspaces "
    sample3 = "NoSpacesHere"
    sample4 = "a\tb\tc"
    sample5 = " leading and trailing spaces "
    print(f"'{sample1}' -> {split_string_by_whitespace(sample1)}")
    print(f"'{sample2}' -> {split_string_by_whitespace(sample2)}")
    print(f"'{sample3}' -> {split_string_by_whitespace(sample3)}")
    print(f"'{sample4}' -> {split_string_by_whitespace(sample4)}")
    print(f"'{sample5}' -> {split_string_by_whitespace(sample5)}")