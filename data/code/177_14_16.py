WHITESPACE = " \t\n\r\f\v"

def split_string_to_words(text):
    words = []
    start = 0
    for i in range(len(text)):
        if text[i] not in WHITESPACE:
            if start == i:
                start = -1
        elif start != -1:
            words.append(text[start:i])
            start = -1
    if start != -1:
        words.append(text[start:])
    return words

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