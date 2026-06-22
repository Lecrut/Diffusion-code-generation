class WordLengthProcessor:
    WORD_PATTERN = r'\w+'
    
    @staticmethod
    def process_text(text: str) -> dict[int, list[str]]:
        if not text:
            return {}
        
        tokens = re.findall(WordLengthProcessor.WORD_PATTERN, text)
        word_lengths = {}
        
        for token in tokens:
            length = len(token)
            if length not in word_lengths:
                word_lengths[length] = []
            word_lengths[length].append(token)
        
        return word_lengths

if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "  Multiple   spaces\tand\nnewlines\nwith punctuation... "
    sample_processor = WordLengthProcessor()
    
    print(f"Input: '{sample_string_1}'")
    result_1 = sample_processor.process_text(sample_string_1)
    print(f"Output: {result_1}\n")
    
    print(f"Input: '{sample_string_2}'")
    result_2 = sample_processor.process_text(sample_string_2)
    print(f"Output: {result_2}\n")