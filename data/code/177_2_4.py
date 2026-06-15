def split_and_filter(text):
    words = text.split()
    return list(words)
if __name__ == '__main__':
    sample1 = "  hello   world  "
    result1 = split_and_filter(sample1)
    print(result1)
    sample2 = "multiple   spaces\tand\ttabs"
    result2 = split_and_filter(sample2)
    print(result2)
    sample3 = " leading and trailing spaces "
    result3 = split_and_filter(sample3)
    print(result3)
    sample4 = "   "
    result4 = split_and_filter(sample4)
    print(result4)