class StringReverser:
    @staticmethod
    def reverse_words(s):
        if not s:
            return s
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
        reversed_words = []
        for word in reversed(words):
            reversed_words.append(word)
        return ' '.join(reversed_words)

if __name__ == '__main__':
    reverser = StringReverser()
    print(reverser.reverse_words("hello world"))
    print(reverser.reverse_words("the quick brown fox"))
    print(reverser.reverse_words("single"))
    print(reverser.reverse_words("  leading spaces"))
    print(reverser.reverse_words("trailing spaces  "))
    print(reverser.reverse_words("multiple   spaces   between"))