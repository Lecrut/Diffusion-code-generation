import re
def count_words(text: str) -> int:
    if not text:
        return 0
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string_1 = "This is a sample string with several words"
    sample_string_2 = "  Multiple   spaces   between   words "
    sample_string_3 = "SingleWord"
    sample_string_4 = ""
    sample_string_5 = "   "
    result1 = count_words(sample_string_1)
    result2 = count_words(sample_string_2)
    result3 = count_words(sample_string_3)
    result4 = count_words(sample_string_4)
    result5 = count_words(sample_string_5)
    print(f"'{sample_string_1}' -> Count: {result1}")
    print(f"'{sample_string_2}' -> Count: {result2}")
    print(f"'{sample_string_3}' -> Count: {result3}")
    print(f"'{sample_string_4}' -> Count: {result4}")
    print(f"'{sample_string_5}' -> Count: {result5}")