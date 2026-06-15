import re
def count_words(text):
    word_list = text.split()
    return len(word_list)
if __name__ == '__main__':
    sample_string1 = "This is a sample string for word counting"
    sample_string2 = "  Multiple   spaces\tand\ttabs\n\nwords here "
    sample_string3 = ""
    sample_string4 = "SingleWord"
    result1 = count_words(sample_string1)
    result2 = count_words(sample_string2)
    result3 = count_words(sample_string3)
    result4 = count_words(sample_string4)
    print(f"'{sample_string1}' has {result1} words")
    print(f"'{sample_string2}' has {result2} words")
    print(f"'{sample_string3}' has {result3} words")
    print(f"'{sample_string4}' has {result4} words")