class RunLengthCompressor:
    SEPARATOR = ""

    @staticmethod
    def _build_segment(char, count):
        return char + str(count)

    @classmethod
    def compress(cls, text):
        if not text:
            return ""
        
        parts = []
        current_char = text[0]
        current_count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                current_count += 1
            else:
                parts.append(cls._build_segment(current_char, current_count))
                current_char = text[i]
                current_count = 1
        
        parts.append(cls._build_segment(current_char, current_count))
        return cls.SEPARATOR.join(parts)

if __name__ == '__main__':
    sample_text = 'hello'
    compressor = RunLengthCompressor()
    print(compressor.compress(sample_text))