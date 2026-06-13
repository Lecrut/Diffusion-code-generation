def split_and_filter(text):
    return [word for word in text.split(' ') if word]
if __name__ == '__main__':
    sample_string1 = "  hello   world  "
    sample_string2 = "one two three"
    sample_string3 = "leading space and multiple spaces"
    sample_string4 = "singleword"
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