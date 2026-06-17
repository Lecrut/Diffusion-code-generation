import re
def count_words(text):
    word_list = text.split()
    return len(word_list)
if __name__ == '__main__':
    sample_string1 = "This is a sample string for word counting"
    sample_string2 = "  Multiple   spaces   between words here  "
    sample_string3 = "SingleWord"
    sample_string4 = ""
    sample_string5 = "Words\twith\nvarious\twhitespace"
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")