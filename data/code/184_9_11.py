import unicodedata

def normalize_and_check(word, text):
    normalized_word = unicodedata.normalize('NFC', word)
    normalized_text = unicodedata.normalize('NFC', text)
    return normalized_word in normalized_text

if __name__ == '__main__':
    sample_word_1 = "critical"
    sample_text_1 = "This is a normal line.\nAnother line without the word.\nThis line is critical and important."
    sample_text_2 = "No critical words here. Just some text."
    sample_text_3 = "\xc3\x89ritical test"

    print(f"Sample 1 result: {normalize_and_check(sample_word_1, sample_text_1)}")
    print(f"Sample 2 result: {normalize_and_check(sample_word_1, sample_text_2)}")
    print(f"Sample 3 result: {normalize_and_check(sample_word_1, sample_text_3)}")