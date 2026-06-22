class StringReverser:
    @staticmethod
    def reverse_words(s):
        if not s:
            return s
        
        result = []
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            j = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            word = s[i + 1:j + 1]
            if result:
                result.append(' ')
            result.append(word)
        
        return ''.join(result)

if __name__ == '__main__':
    s = StringReverser()
    print(s.reverse_words("Hello World"))
    print(s.reverse_words("  abc def  "))
    print(s.reverse_words("SingleWord"))
    print(s.reverse_words(""))
    print(s.reverse_words("  "))