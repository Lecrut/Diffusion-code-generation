class WordReverser:
    @staticmethod
    def reverse_words(s):
        result = []
        current = []
        for char in s:
            if char == ' ':
                if current:
                    result.append(''.join(current))
                    current = []
            else:
                current.append(char)
        if current:
            result.append(''.join(current))
        result.reverse()
        return ' '.join(result)

if __name__ == '__main__':
    reverser = WordReverser()
    test_string = "hello world from python"
    reversed_string = reverser.reverse_words(test_string)
    print(reversed_string)
    test_string2 = "a"
    reversed_string2 = reverser.reverse_words(test_string2)
    print(reversed_string2)
    test_string3 = "  multiple   spaces  between words  "
    reversed_string3 = reverser.reverse_words(test_string3)
    print(reversed_string3)
    test_string4 = ""
    reversed_string4 = reverser.reverse_words(test_string4)
    print(reversed_string4)
    test_string5 = "single"
    reversed_string5 = reverser.reverse_words(test_string5)
    print(reversed_string5)