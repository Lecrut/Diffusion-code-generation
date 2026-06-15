def split_and_filter(text):
    parts = text.split(' ')
    filtered_parts = [part for part in parts if part]
    return filtered_parts
if __name__ == '__main__':
    sample_string1 = "this is a test with   multiple spaces"
    sample_string2 = " leading space and trailing "
    sample_string3 = "singleword"
    sample_string4 = "   multiple   spaces   here"
    sample_string5 = ""
    result1 = split_and_filter(sample_string1)
    result2 = split_and_filter(sample_string2)
    result3 = split_and_filter(sample_string3)
    result4 = split_and_filter(sample_string4)
    result5 = split_and_filter(sample_string5)
    print(f"'{sample_string1}' -> {result1}")
    print(f"'{sample_string2}' -> {result2}")
    print(f"'{sample_string3}' -> {result3}")
    print(f"'{sample_string4}' -> {result4}")
    print(f"'{sample_string5}' -> {result5}")