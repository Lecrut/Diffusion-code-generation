def split_and_filter(text):
    words = text.split()
    return words

if __name__ == '__main__':
    sample1 = "  hello   world  this   is a test "
    sample2 = "singleword"
    sample3 = "   "
    result1 = split_and_filter(sample1)
    result2 = split_and_filter(sample2)
    result3 = split_and_filter(sample3)
    print(f"'{sample1}' -> {result1}")
    print(f"'{sample2}' -> {result2}")
    print(f"'{sample3}' -> {result3}")