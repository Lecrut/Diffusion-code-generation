class WordReverser:
    @staticmethod
    def reverse_words(input_str: str) -> str:
        if not input_str:
            return ""
        
        words = []
        current_word = []
        chars = list(input_str)
        length = len(chars)
        
        for i in range(length):
            char = chars[i]
            if char == ' ':
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            else:
                current_word.append(char)
        
        if current_word:
            words.append(''.join(current_word))
        
        return ' '.join(reversed(words))

if __name__ == '__main__':
    solver = WordReverser()
    result = solver.reverse_words("Hello World")
    print(result)