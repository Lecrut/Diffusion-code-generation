import unicodedata

def check_word_in_unicode_string(target_word, unicode_string):
    normalized_target = unicodedata.normalize('NFC', target_word)
    normalized_string = unicodedata.normalize('NFC', unicode_string)
    return normalized_target in normalized_string

if __name__ == '__main__':
    sample_word_1 = "example"
    sample_unicode_string_1 = "This is an example sentence. Example words are everywhere."
    sample_word_2 = "sample"
    sample_unicode_string_2 = "No samples here. Just some text."

    print(f"Does '{sample_word_1}' exist in the string? {check_word_in_unicode_string(sample_word_1, sample_unicode_string_1)}")
    print(f"Does '{sample_word_2}' exist in the string? {check_word_in_unicode_string(sample_word_2, sample_unicode_string_2)}")