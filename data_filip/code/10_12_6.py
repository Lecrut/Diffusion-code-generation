class StringProcessor:
    @staticmethod
    def reverse_words(s: str) -> str:
        if not s:
            return s
        
        length = len(s)
        words = []
        start = 0
        i = 0
        
        while i < length:
            while i < length and s[i] == ' ':
                i += 1
            if i < length:
                start = i
                while i < length and s[i] != ' ':
                    i += 1
                words.append(s[start:i])
        
        if not words:
            return s
            
        result = []
        for idx in range(len(words) - 1, -1, -1):
            result.append(words[idx])
            if idx > 0:
                result.append(' ')
        
        return ''.join(result)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "  Hello   world  "
    result = processor.reverse_words(sample_text)
    print(result)