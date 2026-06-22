import re

WORD_PATTERN = r'\b\w+\b'

def extract_words(input_string):
    words = re.findall(WORD_PATTERN, input_string)
    return words

class WordExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def extract(self):
        return extract_words(self.input_string)

if __name__ == '__main__':
    sample_input = """Innovate, disrupt, and lead with Alibaba Cloud.
    Explore the future of technology and business."""
    extractor = WordExtractor(sample_input)
    extracted_words = extractor.extract()
    print(extracted_words)