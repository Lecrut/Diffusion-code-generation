def extract_first_word(sentence: str) -> str:
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_sentence_1 = "Hello world, this is a test."
    sample_sentence_2 = "  \t\n  Another line starts here."
    sample_sentence_3 = "123numbers and symbols"
    sample_sentence_4 = ""
    sample_sentence_5 = "   "
    print(f"Input: '{sample_sentence_1}' -> First Word: '{extract_first_word(sample_sentence_1)}'")
    print(f"Input: '{sample_sentence_2}' -> First Word: '{extract_first_word(sample_sentence_2)}'")
    print(f"Input: '{sample_sentence_3}' -> First Word: '{extract_first_word(sample_sentence_3)}'")
    print(f"Input: '{sample_sentence_4}' -> First Word: '{extract_first_word(sample_sentence_4)}'")
    print(f"Input: '{sample_sentence_5}' -> First Word: '{extract_first_word(sample_sentence_5)}'")