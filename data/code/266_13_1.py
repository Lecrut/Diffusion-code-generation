import re
def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    sample1 = "This is a sample sentence."
    sample2 = "  Multiple   spaces   here."
    sample3 = ""
    sample4 = "SingleWord"
    print(f"'{sample1}': {count_words(sample1)}")
    print(f"'{sample2}': {count_words(sample2)}")
    print(f"'{sample3}': {count_words(sample3)}")
    print(f"'{sample4}': {count_words(sample4)}")