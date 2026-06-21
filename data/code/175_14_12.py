class SentenceProcessor:
    def split_sentence(self, sentence: str) -> list[str]:
        words = []
        word_buffer = []
        
        for char in sentence:
            if char == ' ':
                if word_buffer:
                    words.append(''.join(word_buffer))
                    word_buffer.clear()
            else:
                word_buffer.append(char)
        
        if word_buffer:
            words.append(''.join(word_buffer))
        
        return words

if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentence = "  Hello world! This is a test with multiple   spaces. "
    tokens = processor.split_sentence(sample_sentence)
    print(tokens)