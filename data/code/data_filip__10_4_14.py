def _normalize_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text.strip():
        return []
    return text.split()

def reverse_word_order(text):
    word_list = _normalize_input(text)
    word_list.reverse()
    return ' '.join(word_list)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    result = reverse_word_order(sample_text)
    print(result)