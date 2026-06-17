import re
def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    sample1 = "This is a sample sentence."
    sample2 = "  leading and trailing spaces are handled correctly "
    sample3 = "OneWord"
    sample4 = ""
    sample5 = "Multiple   spaces\tand\nnewlines"
    print(f"'{sample1}': {count_words(sample1)}")
    print(f"'{sample2}': {count_words(sample2)}")
    print(f"'{sample3}': {count_words(sample3)}")
    print(f"'{sample4}': {count_words(sample4)}")
    print(f"'{sample5}': {count_words(sample5)}")