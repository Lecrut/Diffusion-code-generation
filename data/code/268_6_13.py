def get_first_word(sentence: str) -> str:
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_text_1 = "Hello world, this is a test."
    sample_text_2 = "  \t\n  Another line starts here."
    sample_text_3 = "123numbers and symbols"
    sample_text_4 = ""
    sample_text_5 = "   "
    print(f"Input: '{sample_text_1}' -> First Word: '{get_first_word(sample_text_1)}'")
    print(f"Input: '{sample_text_2}' -> First Word: '{get_first_word(sample_text_2)}'")
    print(f"Input: '{sample_text_3}' -> First Word: '{get_first_word(sample_text_3)}'")
    print(f"Input: '{sample_text_4}' -> First Word: '{get_first_word(sample_text_4)}'")
    print(f"Input: '{sample_text_5}' -> First Word: '{get_first_word(sample_text_5)}'")