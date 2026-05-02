import string
def get_first_letters(text):
    word_dict = {}
    words = text.split()
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            word_dict[cleaned_word] = cleaned_word[0]
    return word_dict
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test."
    sample_string2 = "Python is fun, isn't it?"
    sample_string3 = "  What's up?  End."
    result1 = get_first_letters(sample_string1)
    result2 = get_first_letters(sample_string2)
    result3 = get_first_letters(sample_string3)
    print(f"'{sample_string1}' -> {result1}")
    print(f"'{sample_string2}' -> {result2}")
    print(f"'{sample_string3}' -> {result3}")