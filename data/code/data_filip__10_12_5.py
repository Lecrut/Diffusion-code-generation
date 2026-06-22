class StringReverser:
    @staticmethod
    def reverse_words(text: str) -> str:
        if not text:
            return ""
        
        result = []
        current_word_start = None
        
        for i, char in enumerate(text):
            if char != ' ':
                if current_word_start is None:
                    current_word_start = i
            else:
                if current_word_start is not None:
                    result.append(text[current_word_start:i])
                    current_word_start = None
        
        if current_word_start is not None:
            result.append(text[current_word_start:])
        
        result.reverse()
        return ' '.join(result)

if __name__ == '__main__':
    sample_text = "  hello   world  this is a test  "
    reversed_text = StringReverser.reverse_words(sample_text)
    print(reversed_text)