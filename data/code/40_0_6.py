import sys
def first_letter_of_words(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return "".join(first_letters)
if __name__ == '__main__':
    sample_string_1 = "  Hello world, this is a test. "
    sample_string_2 = "   multiple   spaces   between   words "
    sample_string_3 = "singleword"
    sample_string_4 = ""
    sample_string_5 = "  leading and trailing spaces "
    print(f"Input: '{sample_string_1}' -> Output: {first_letter_of_words(sample_string_1)}")
    print(f"Input: '{sample_string_2}' -> Output: {first_letter_of_words(sample_string_2)}")
    print(f"Input: '{sample_string_3}' -> Output: {first_letter_of_words(sample_string_3)}")
    print(f"Input: '{sample_string_4}' -> Output: {first_letter_of_words(sample_string_4)}")
    print(f"Input: '{sample_string_5}' -> Output: {first_letter_of_words(sample_string_5)}")