import re
def split_and_filter(text):
    words = re.split(r'\s+', text)
    non_empty_words = [word for word in words if word]
    return non_empty_words
if __name__ == '__main__':
    sample_string1 = "This is a test string with   multiple spaces"
    sample_string2 = "  leading and trailing spaces   "
    sample_string3 = "singleword"
    sample_string4 = "   "
    sample_string5 = "word1  word2\tword3\nword4"
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