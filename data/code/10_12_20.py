class WordReverser:
    @staticmethod
    def reverse_words(s):
        if not s:
            return s
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                start = i
                while i >= 0 and s[i] != ' ':
                    i -= 1
                result.append(s[i + 1:start + 1])
            i -= 1
        return ' '.join(result)

if __name__ == '__main__':
    reverser = WordReverser()
    print(reverser.reverse_words("hello world"))
    print(reverser.reverse_words("Python is great"))
    print(reverser.reverse_words("  multiple   spaces  "))
    print(reverser.reverse_words("singleword"))
    print(reverser.reverse_words(""))