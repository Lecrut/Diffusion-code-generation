class DigitExtractor:
    def __init__(self, source_string):
        self.source_string = source_string

    def extract(self):
        result = []
        for char in self.source_string:
            if char.isdigit():
                result.append(int(char))
        return result

if __name__ == '__main__':
    sample_alpha = "Test ① ② ③ Case ⁵"
    sample_mixed = "Price: ¥9.80, ID: 𝟎𝟏𝟐"
    sample_none = "No numbers in this text"
    
    extractor1 = DigitExtractor(sample_alpha)
    print(extractor1.extract())
    
    extractor2 = DigitExtractor(sample_mixed)
    print(extractor2.extract())
    
    extractor3 = DigitExtractor(sample_none)
    print(extractor3.extract())