import unicodedata

def normalize_and_check(word, text):
    normalized_word = unicodedata.normalize('NFC', word)
    normalized_text = unicodedata.normalize('NFC', text)
    return normalized_word in normalized_text

if __name__ == '__main__':
    SAMPLE_WORD_1 = "example"
    SAMPLE_TEXT_1 = "This is an example sentence."
    SAMPLE_TEXT_2 = "No match here."

    print(f"Sample 1 result: {normalize_and_check(SAMPLE_WORD_1, SAMPLE_TEXT_1)}")
    print(f"Sample 2 result: {normalize_and_check(SAMPLE_WORD_1, SAMPLE_TEXT_2)}")