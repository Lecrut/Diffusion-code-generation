class StringReverser:
    @staticmethod
    def reverse_words(s: str) -> str:
        if not s:
            return ""
        
        words = []
        current_word = []
        for char in s:
            if char == ' ':
                if current_word:
                    words.append("".join(current_word))
                    current_word = []
            else:
                current_word.append(char)
        if current_word:
            words.append("".join(current_word))
        
        words.reverse()
        return " ".join(words)

if __name__ == '__main__':
    result = StringReverser.reverse_words("the sky is blue")
    print(result)
    
    result2 = StringReverser.reverse_words("  hello   world  ")
    print(result2)
    
    result3 = StringReverser.reverse_words("")
    print(result3)