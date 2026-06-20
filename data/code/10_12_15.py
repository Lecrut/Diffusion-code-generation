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
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

if __name__ == '__main__':
    reverser = StringReverser()
    test_cases = [
        "hello world",
        "the sky is blue",
        "a",
        "  hello   world  ",
        ""
    ]
    for case in test_cases:
        result = reverser.reverse_words(case)
        print(repr(result))