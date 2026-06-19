import re

def get_first_letters(text):
    words = re.findall(r'\b\w', text)
    return ''.join(words)

if __name__ == '__main__':
    sample_string_1 = "  Hello world, this is a test "
    sample_string_2 = "multiple   spaces\tand\nnewlines"
    sample_string_3 = "singleword"
    sample_string_4 = "   "
    sample_string_5 = ""
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