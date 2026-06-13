import re
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    sample_string1 = "hello world this is a test"
    result1 = reverse_words(sample_string1)
    print(f"Original: '{sample_string1}'")
    print(f"Reversed: '{result1}'")
    sample_string2 = "optimization is key"
    result2 = reverse_words(sample_string2)
    print(f"Original: '{sample_string2}'")
    print(f"Reversed: '{result2}'")
    sample_string3 = "  leading and trailing spaces   "
    result3 = reverse_words(sample_string3)
    print(f"Original: '{sample_string3}'")
    print(f"Reversed: '{result3}'")