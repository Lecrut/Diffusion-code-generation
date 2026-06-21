import unicodedata

def contains_word_nfc(text, word):
    normalized_text = unicodedata.normalize('NFC', text)
    return word in normalized_text

if __name__ == '__main__':
    sample_text = "Hello, 世界!"
    search_word = "世"
    result = contains_word_nfc(sample_text, search_word)
    print(result)