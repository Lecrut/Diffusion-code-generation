import re
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "  the quick brown fox  "
    sample3 = "  multiple   spaces   here "
    sample4 = "singleword"
    sample5 = ""
    sample6 = "   "
    print(f"'{sample1}' -> '{reverse_words(sample1)}'")
    print(f"'{sample2}' -> '{reverse_words(sample2)}'")
    print(f"'{sample3}' -> '{reverse_words(sample3)}'")
    print(f"'{sample4}' -> '{reverse_words(sample4)}'")
    print(f"'{sample5}' -> '{reverse_words(sample5)}'")
    print(f"'{sample6}' -> '{reverse_words(sample6)}'")