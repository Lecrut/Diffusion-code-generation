def split_string_by_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample1 = "Hello world"
    print(f"Input: '{sample1}'")
    print(f"Output: {split_string_by_whitespace(sample1)}")

    sample2 = "  This   has\tmultiple\nspaces "
    print(f"Input: '{sample2}'")
    print(f"Output: {split_string_by_whitespace(sample2)}")

    sample3 = "NoSpacesHere"
    print(f"Input: '{sample3}'")
    print(f"Output: {split_string_by_whitespace(sample3)}")

    sample4 = "\t\n leading and trailing \r spaces"
    print(f"Input: '{sample4}'")
    print(f"Output: {split_string_by_whitespace(sample4)}")