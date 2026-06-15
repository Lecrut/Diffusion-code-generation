import re
def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    sample1 = "  hello   world  "
    sample2 = "this   is   a   test"
    sample3 = "singleword"
    sample4 = "   leading and trailing spaces   "
    sample5 = ""
    sample6 = "   "
    print(f"Input: '{sample1}' -> Output: '{reverse_word_order(sample1)}'")
    print(f"Input: '{sample2}' -> Output: '{reverse_word_order(sample2)}'")
    print(f"Input: '{sample3}' -> Output: '{reverse_word_order(sample3)}'")
    print(f"Input: '{sample4}' -> Output: '{reverse_word_order(sample4)}'")
    print(f"Input: '{sample5}' -> Output: '{reverse_word_order(sample5)}'")
    print(f"Input: '{sample6}' -> Output: '{reverse_word_order(sample6)}'")