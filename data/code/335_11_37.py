import re
class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in re.split(r'\s+', sentence.strip()) if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello   world", "Python is great.", "", "Multiple   spaces   here"]
    results = []
    for s in sample_sentences:
        words = processor.split_sentence(s)
        results.append(f"Input: '{s}' -> Output: {words}")
    print("\n".join(results))