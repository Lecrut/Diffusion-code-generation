def split_and_filter(text):
    return [word for word in text.split(' ') if word]
if __name__ == '__main__':
    sample_string1 = "  hello   world  "
    result1 = split_and_filter(sample_string1)
    print(result1)
    sample_string2 = "one two three"
    result2 = split_and_filter(sample_string2)
    print(result2)
    sample_string3 = "leading space and multiple   spaces"
    result3 = split_and_filter(sample_string3)
    print(result3)
    sample_string4 = "singleword"
    result4 = split_and_filter(sample_string4)
    print(result4)