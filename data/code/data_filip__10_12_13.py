class WordReverser:
    @staticmethod
    def reverse_words(s: str) -> str:
        if not s:
            return ""
        
        result = []
        length = len(s)
        start = 0
        
        while start < length:
            if s[start] != ' ':
                end = start
                while end < length and s[end] != ' ':
                    end += 1
                result.append(s[start:end])
                start = end
            else:
                start += 1
        
        return ' '.join(reversed(result))

if __name__ == '__main__':
    reverser = WordReverser()
    sample_input = "hello world"
    output = reverser.reverse_words(sample_input)
    print(output)