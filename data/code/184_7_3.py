class StringProcessor:
    def __init__(self):
        pass
    def contains_target_words(self, text, target_words):
        found_words = set()
        text_lower = text.lower()
        for word in target_words:
            if word.lower() in text_lower:
                found_words.add(word)
        return found_words
if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "The quick brown fox jumps over the lazy dog and the fox is clever"
    target_words_list = ["fox", "dog", "cat"]
    found = processor.contains_target_words(sample_text, target_words_list)
    print(found)