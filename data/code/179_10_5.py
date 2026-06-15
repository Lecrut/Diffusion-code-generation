import sys
def reverse_word_order(input_string):
    words = input_string.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    test_cases = [
        "Hello world",
        "  leading and trailing spaces ",
        "multiple   spaces here",
        "singleword",
        "",
        "   ",
        "one two three"
    ]
    for test in test_cases:
        result = reverse_word_order(test)
        print(f"Input: '{test}'")
        print(f"Output: '{result}'")
        print("-" * 20)