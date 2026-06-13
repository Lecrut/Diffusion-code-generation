def split_and_filter(text):
    return [word for word in text.split(' ') if word]
if __name__ == '__main__':
    sample_string1 = "this   is a test with multiple spaces"
    result1 = split_and_filter(sample_string1)
    print(result1)
    sample_string2 = " leading space and trailing space "
    result2 = split_and_filter(sample_string2)
    print(result2)
    sample_string3 = "singleword"
    result3 = split_and_filter(sample_string3)
    print(result3)
    sample_string4 = "   "
    result4 = split_and_filter(sample_string4)
    print(result4)