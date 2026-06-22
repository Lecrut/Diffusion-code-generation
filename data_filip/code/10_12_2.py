class StringReverser:
    @staticmethod
    def reverse_words(text):
        if not text:
            return ""
        words = []
        current_word = []
        for char in text:
            if char == ' ':
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
                words.append(' ')
            else:
                current_word.append(char)
        if current_word:
            words.append(''.join(current_word))
        words.reverse()
        return ''.join(words)

if __name__ == '__main__':
    sample_text = "  hello world  from  Python  "
    reversed_text = StringReverser.reverse_words(sample_text)
    print(reversed_text)