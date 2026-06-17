def count_words(text):
    word_list = text.split()
    return len(word_list)
if __name__ == '__main__':
    sample_string1 = "This is a sample string for testing"
    sample_string2 = "  Multiple   spaces   between words here "
    sample_string3 = "SingleWord"
    sample_string4 = ""
    sample_string5 = "   \t\n"
    print(f"'{sample_string1}' has {count_words(sample_string1)} words.")
    print(f"'{sample_string2}' has {count_words(sample_string2)} words.")
    print(f"'{sample_string3}' has {count_words(sample_string3)} words.")
    print(f"'{sample_string4}' has {count_words(sample_string4)} words.")
    print(f"'{sample_string5}' has {count_words(sample_string5)} words.")