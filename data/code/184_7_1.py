class StringProcessor:
    def __init__(self):
        pass
    def contains_any_target(self, text, target_words):
        found_words = set()
        text_lower = text.lower()
        for word in target_words:
            if word.lower() in text_lower.split():
                found_words.add(word)
        return found_words
if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "This is a test string containing some words like apple and banana."
    target_words = ["apple", "orange", "grape"]
    result = processor.contains_any_target(sample_text, target_words)
    print(result)