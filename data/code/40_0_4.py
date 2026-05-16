import sys
def get_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return "".join(first_letters)
if __name__ == '__main__':
    sample_string_1 = "  Hello world   this is a test "
    sample_string_2 = "singleword"
    sample_string_3 = "   leading space test"
    sample_string_4 = ""
    sample_string_5 = "word1  word2   word3"
    print(f"Input: '{sample_string_1}' -> Output: {get_first_letters(sample_string_1)}")
    print(f"Input: '{sample_string_2}' -> Output: {get_first_letters(sample_string_2)}")
    print(f"Input: '{sample_string_3}' -> Output: {get_first_letters(sample_string_3)}")
    print(f"Input: '{sample_string_4}' -> Output: {get_first_letters(sample_string_4)}")
    print(f"Input: '{sample_string_5}' -> Output: {get_first_letters(sample_string_5)}")