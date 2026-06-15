import re
def count_words(text: str) -> int:
    if not text:
        return 0
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string_1 = "This is a sample string with multiple words"
    sample_string_2 = "  leading and trailing spaces   are handled correctly "
    sample_string_3 = "SingleWord"
    sample_string_4 = ""
    sample_string_5 = "  \t\nMultiple\tspaces\r"
    print(f"'{sample_string_1}' has {count_words(sample_string_1)} words")
    print(f"'{sample_string_2}' has {count_words(sample_string_2)} words")
    print(f"'{sample_string_3}' has {count_words(sample_string_3)} words")
    print(f"'{sample_string_4}' has {count_words(sample_string_4)} words")
    print(f"'{sample_string_5}' has {count_words(sample_string_5)} words")