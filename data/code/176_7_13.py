PARAGRAPH = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
DISTINCT_WORDS_KEY = 'distinct_words'

class ParagraphProcessor:

    def __init__(self, paragraph):
        self.paragraph = paragraph

    def parse(self):
        words = self.paragraph.split()
        distinct_words = sorted(set(words))
        return {DISTINCT_WORDS_KEY: distinct_words}
if __name__ == '__main__':
    processor_instance = ParagraphProcessor(PARAGRAPH)
    result = processor_instance.parse()
    print(result[DISTINCT_WORDS_KEY])