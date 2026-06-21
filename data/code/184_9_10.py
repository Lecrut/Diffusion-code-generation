import unicodedata

def normalize_and_check(word, text):
    normalized_word = unicodedata.normalize('NFC', word)
    normalized_text = unicodedata.normalize('NFC', text)
    return normalized_word in normalized_text

if __name__ == '__main__':
    sample_word_1 = "example"
    sample_word_2 = "EXAMPLE"
    sample_word_3 = "exAmple"
    
    sample_text_1 = "This is an example sentence."
    sample_text_2 = "No match here."
    sample_text_3 = "\u00e9xample with special characters."

    print(f"Sample 1 result: {normalize_and_check(sample_word_1, sample_text_1)}")
    print(f"Sample 2 result: {normalize_and_check(sample_word_2, sample_text_2)}")
    print(f"Sample 3 result: {normalize_and_check(sample_word_3, sample_text_3)}")