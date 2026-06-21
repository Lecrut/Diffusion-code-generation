def split_and_clean(text):
    parts = text.split()
    return parts

if __name__ == '__main__':
    sample_input1 = "this is a test"
    result1 = split_and_clean(sample_input1)
    print(f"Input: '{sample_input1}'")
    print(f"Output: {result1}")

    sample_input2 = "  leading and trailing spaces "
    result2 = split_and_clean(sample_input2)
    print(f"Input: '{sample_input2}'")
    print(f"Output: {result2}")

    sample_input3 = "singleword"
    result3 = split_and_clean(sample_input3)
    print(f"Input: '{sample_input3}'")
    print(f"Output: {result3}")

    sample_input4 = "   multiple   spaces   here "
    result4 = split_and_clean(sample_input4)
    print(f"Input: '{sample_input4}'")
    print(f"Output: {result4}")