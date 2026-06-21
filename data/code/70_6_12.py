class LargeStringProcessor:
    WORD_SEPARATOR = " "
    EMPTY_RESULT = (None, None)

    def __init__(self, raw_text):
        if not isinstance(raw_text, str):
            raise ValueError("Input must be a string")
        self.raw_text = raw_text

    @staticmethod
    def _get_word_boundary(text, index):
        if index <= 0 or index >= len(text):
            return index
        if text[index] != LargeStringProcessor.WORD_SEPARATOR:
            return index
        forward = index
        while forward < len(text) and text[forward] == LargeStringProcessor.WORD_SEPARATOR:
            forward += 1
        return forward

    def get_first_and_last_words(self):
        text = self.raw_text
        if not text:
            return LargeStringProcessor.EMPTY_RESULT
        
        start_index = 0
        while start_index < len(text) and text[start_index] == LargeStringProcessor.WORD_SEPARATOR:
            start_index += 1
        
        if start_index == len(text):
            return LargeStringProcessor.EMPTY_RESULT
        
        end_index = len(text) - 1
        while end_index >= 0 and text[end_index] == LargeStringProcessor.WORD_SEPARATOR:
            end_index -= 1
        
        if start_index > end_index:
            return LargeStringProcessor.EMPTY_RESULT
        
        first_word_start = start_index
        last_word_end = end_index + 1
        
        first_word = ""
        while first_word_start < len(text) and text[first_word_start] != LargeStringProcessor.WORD_SEPARATOR:
            first_word += text[first_word_start]
            first_word_start += 1
        
        last_word = ""
        while last_word_end > first_word_start:
            last_word_end -= 1
            last_word = text[last_word_end] + last_word
            
        return first_word, last_word

if __name__ == '__main__':
    sample_text = "  Leading spaces   middle words   trailing spaces  "
    processor = LargeStringProcessor(sample_text)
    first, last = processor.get_first_and_last_words()
    print(first)
    print(last)