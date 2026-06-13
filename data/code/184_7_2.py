class StringProcessor:
    def __init__(self):
        pass
    def contains_target_words(self, text, target_words):
        found_words = set()
        text_lower = text.lower()
        for word in target_words:
            if word.lower() in text_lower.split():
                found_words.add(word)
        return found_words
if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "This is a sample text containing some words like apple and banana."
    target_words_set = ["apple", "orange", "grape"]
    found = processor.contains_target_words(sample_text, target_words_set)
    print(found)