import re
def count_words(text):
    if not text:
        return 0
    return len(re.findall(r'\b\w+\b', text))
if __name__ == '__main__':
    sample_string1 = "This is a sample sentence with varying amounts of whitespace."
    sample_string2 = "  Multiple   spaces   here \t and newlines\n."
    sample_string3 = ""
    sample_string4 = "SingleWord"
    sample_string5 = "Word1\nWord2"
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")