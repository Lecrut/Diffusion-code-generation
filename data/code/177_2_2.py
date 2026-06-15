def split_and_filter(text):
    words = text.split()
    return list(words)
if __name__ == '__main__':
    sample_string1 = "  hello   world  this   is a test "
    result1 = split_and_filter(sample_string1)
    print(result1)
    sample_string2 = "singleword"
    result2 = split_and_filter(sample_string2)
    print(result2)
    sample_string3 = "   "
    result3 = split_and_filter(sample_string3)
    print(result3)
    sample_string4 = ""
    result4 = split_and_filter(sample_string4)
    print(result4)