import re
def count_words(text):
    if not text:
        return 0
    return len(re.findall(r'\b\w+\b', text))
if __name__ == '__main__':
    sample_string1 = "This is a sample string with varying amounts of whitespace."
    sample_string2 = "  leading and trailing spaces   \tand multiple spaces in between. "
    sample_string3 = ""
    sample_string4 = "One\nTwo\tThree"
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")