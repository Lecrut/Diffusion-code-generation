class StringReverser:
    @staticmethod
    def reverse_words(s):
        words = []
        current_word = []
        for char in s:
            if char == ' ':
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            else:
                current_word.append(char)
        if current_word:
            words.append(''.join(current_word))
        
        result = []
        for i in range(len(words) - 1, -1, -1):
            if result:
                result.append(' ')
            result.append(words[i])
        
        return ''.join(result)

if __name__ == '__main__':
    sr = StringReverser()
    print(sr.reverse_words("hello world"))
    print(sr.reverse_words("a b c"))
    print(sr.reverse_words("  leading spaces"))
    print(sr.reverse_words("trailing spaces  "))
    print(sr.reverse_words("  multiple   spaces  between  words  "))
    print(sr.reverse_words(""))
    print(sr.reverse_words("single"))