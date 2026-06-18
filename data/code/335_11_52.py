import re
class SentenceProcessor:
    def __init__(self):
        self.regex = re.compile(r'\s+')
    def split_sentence(self, sentence):
        return [word for word in self.regex.split(sentence) if len(word.strip()) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello   world", "Python is     great\nand fun.", ""]
    for sentence in sample_sentences:
        words = processor.split_sentence(sentence)
        print(f"{sentence!r} -> {words}")