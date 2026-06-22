class WordReverser:
    @staticmethod
    def reverse_words(text):
        if not text:
            return ""
        
        words = []
        start = 0
        length = len(text)
        
        while start < length:
            if text[start] != ' ':
                end = start + 1
                while end < length and text[end] != ' ':
                    end += 1
                words.append(text[start:end])
                start = end
            else:
                start += 1
                
        result_parts = []
        for word in reversed(words):
            result_parts.append(word)
            
        return " ".join(result_parts)

if __name__ == '__main__':
    print(WordReverser.reverse_words("the sky is blue"))
    print(WordReverser.reverse_words("  hello   world  "))
    print(WordReverser.reverse_words("a"))
    print(WordReverser.reverse_words(""))