import sys
def get_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return "".join(first_letters)
if __name__ == '__main__':
    sample_string_1 = "  Hello world  this is a test "
    sample_string_2 = "multiple   spaces   between words"
    sample_string_3 = "singleword"
    sample_string_4 = "  "
    sample_string_5 = "word1 word2\tword3\nword4"
    print(f"Input: '{sample_string_1}'")
    print("Output:", get_first_letters(sample_string_1))
    print("-" * 20)
    print(f"Input: '{sample_string_2}'")
    print("Output:", get_first_letters(sample_string_2))
    print("-" * 20)
    print(f"Input: '{sample_string_3}'")
    print("Output:", get_first_letters(sample_string_3))
    print("-" * 20)
    print(f"Input: '{sample_string_4}'")
    print("Output:", get_first_letters(sample_string_4))
    print("-" * 20)
    print(f"Input: '{sample_string_5}'")
    print("Output:", get_first_letters(sample_string_5))
    print("-" * 20)