class KeywordSearcher:
    KEYWORDS = ["quick", "fox", "lazy", "cat"]

    @staticmethod
    def search_keywords(text):
        text_lower = text.lower()
        return {word: text_lower.count(word.lower()) for word in KeywordSearcher.KEYWORDS if word.lower() in text_lower}

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog fox"
    searcher = KeywordSearcher()
    result = searcher.search_keywords(sample_text)
    print(result)