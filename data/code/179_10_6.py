import sys
def reverse_word_order(input_string):
    words = input_string.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    sample1 = "  Hello world   this is a test "
    sample2 = "singleword"
    sample3 = "   multiple   spaces   here"
    sample4 = ""
    sample5 = "   "
    print(f"Input: '{sample1}'")
    print("Output:", reverse_word_order(sample1))
    print("-" * 20)
    print(f"Input: '{sample2}'")
    print("Output:", reverse_word_order(sample2))
    print("-" * 20)
    print(f"Input: '{sample3}'")
    print("Output:", reverse_word_order(sample3))
    print("-" * 20)
    print(f"Input: '{sample4}'")
    print("Output:", reverse_word_order(sample4))
    print("-" * 20)
    print(f"Input: '{sample5}'")
    print("Output:", reverse_word_order(sample5))
    print("-" * 20)