def split_and_filter(text):
    return [part for part in text.split(' ') if part]

if __name__ == '__main__':
    sample1 = "this is a test"
    result1 = split_and_filter(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")
    
    sample2 = "  leading and trailing spaces "
    result2 = split_and_filter(sample2)
    print(f"Input: '{sample2}'")
    print(f"Output: {result2}")
    
    sample3 = "singleword"
    result3 = split_and_filter(sample3)
    print(f"Input: '{sample3}'")
    print(f"Output: {result3}")
    
    sample4 = "   "
    result4 = split_and_filter(sample4)
    print(f"Input: '{sample4}'")
    print(f"Output: {result4}")