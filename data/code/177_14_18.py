def split_string_to_words(text):
    return text.split()

if __name__ == '__main__':
    sample1 = "  hello world  "
    result1 = split_string_to_words(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")

    sample2 = "multiple   spaces here"
    result2 = split_string_to_words(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")

    sample3 = " leading and trailing "
    result3 = split_string_to_words(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")

    sample4 = ""
    result4 = split_string_to_words(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")