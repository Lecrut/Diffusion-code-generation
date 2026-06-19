class Segmenter:
    DELIMITERS = []

    @staticmethod
    def set_delimiters(delimiters):
        Segmenter.DELIMITERS = delimiters

    @staticmethod
    def segment_phrase(phrase):
        segments = []
        current_segment = ""
        for char in phrase:
            if char in Segmenter.DELIMITERS:
                if current_segment:
                    segments.append(current_segment)
                current_segment = ""
            else:
                current_segment += char
        if current_segment:
            segments.append(current_segment)
        return segments

if __name__ == '__main__':
    sample_phrase = "apple,banana;orange,grape"
    sample_delimiters = [',', ';']
    
    Segmenter.set_delimiters(sample_delimiters)
    result = Segmenter.segment_phrase(sample_phrase)
    print(result)