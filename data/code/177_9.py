import re
def split_string_by_whitespace(text):
    return re.split(r'\s+', text)
if __name__ == '__main__':
    sample1 = "Hello world"
    result1 = split_string_by_whitespace(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")
    sample2 = "  This   has\tmultiple\nspaces "
    result2 = split_string_by_whitespace(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")
    sample3 = "NoSpacesHere"
    result3 = split_string_by_whitespace(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")
    sample4 = "a\t\nb\r\n c"
    result4 = split_string_by_whitespace(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")