def split_and_filter(text):
    return [part for part in text.split() if part]

if __name__ == '__main__':
    sample1 = "this is a test"
    print(f"Input: '{sample1}'")
    print(f"Output: {split_and_filter(sample1)}")

    sample2 = "  leading and trailing spaces "
    print(f"Input: '{sample2}'")
    print(f"Output: {split_and_filter(sample2)}")

    sample3 = "singleword"
    print(f"Input: '{sample3}'")
    print(f"Output: {split_and_filter(sample3)}")

    sample4 = "   "
    print(f"Input: '{sample4}'")
    print(f"Output: {split_and_filter(sample4)}")