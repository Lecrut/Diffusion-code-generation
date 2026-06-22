import re

class PatternExtractor:
    def __init__(self, text):
        self.text = text

    def extract_all_non_overlapping(self, pattern):
        return re.findall(pattern, self.text)

if __name__ == '__main__':
    sample_text = "apple banana apple orange apple"
    extractor = PatternExtractor(sample_text)
    
    pattern1 = r"apple"
    result1 = extractor.extract_all_non_overlapping(pattern1)
    print(result1)
    
    pattern2 = r"\bapple\b"
    result2 = extractor.extract_all_non_overlapping(pattern2)
    print(result2)