class PhraseSegmenter:
    def __init__(self, phrase, delimiters):
        self.phrase = phrase
        self.delimiters = set(delimiters)
        self.segments = []

    def segment(self):
        current_segment = ""
        for char in self.phrase:
            if char in self.delimiters:
                if current_segment:
                    self.segments.append(current_segment)
                current_segment = ""
            else:
                current_segment += char
        if current_segment:
            self.segments.append(current_segment)
        return self.segments

if __name__ == '__main__':
    sample_phrase = "apple,banana;orange,grape"
    sample_delimiters = [',', ';']
    
    segmenter = PhraseSegmenter(sample_phrase, sample_delimiters)
    result = segmenter.segment()
    print(f"Segments: {result}")