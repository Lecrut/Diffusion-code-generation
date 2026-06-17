import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample_string1 = "This is a sample string with various spaces."
    sample_string2 = "  leading and trailing spaces   \tand multiple spaces\n\nbetween them."
    sample_string3 = "SingleWord"
    sample_string4 = ""
    sample_string5 = "  \t \n "
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")