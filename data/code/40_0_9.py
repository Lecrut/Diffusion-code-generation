import sys
def get_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return "".join(first_letters)
if __name__ == '__main__':
    sample_string_1 = "  Hello world!   this is a test "
    sample_string_2 = "singleword"
    sample_string_3 = "   leading spaces and multiple   spaces "
    sample_string_4 = ""
    sample_string_5 = "one two three"
    print(f"Input: '{sample_string_1}'")
    print(get_first_letters(sample_string_1))
    print("-" * 20)
    print(f"Input: '{sample_string_2}'")
    print(get_first_letters(sample_string_2))
    print("-" * 20)
    print(f"Input: '{sample_string_3}'")
    print(get_first_letters(sample_string_3))
    print("-" * 20)
    print(f"Input: '{sample_string_4}'")
    print(get_first_letters(sample_string_4))
    print("-" * 20)
    print(f"Input: '{sample_string_5}'")
    print(get_first_letters(sample_string_5))
    print("-" * 20)