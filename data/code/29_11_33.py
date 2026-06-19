class StringReverser:
    def __init__(self, word):
        self.word = list(word)

    def reverse(self):
        left, right = 0, len(self.word) - 1
        while left < right:
            self.word[left], self.word[right] = self.word[right], self.word[left]
            left += 1
            right -= 1

    def get_reversed_word(self):
        return ''.join(self.word)

if __name__ == '__main__':
    test_string1 = "hello"
    reverser1 = StringReverser(test_string1)
    reverser1.reverse()
    print(f"'{test_string1}' reversed is '{reverser1.get_reversed_word()}'")

    test_string2 = "world"
    reverser2 = StringReverser(test_string2)
    reverser2.reverse()
    print(f"'{test_string2}' reversed is '{reverser2.get_reversed_word()}'")

    test_string3 = "Python"
    reverser3 = StringReverser(test_string3)
    reverser3.reverse()
    print(f"'{test_string3}' reversed is '{reverser3.get_reversed_word()}'")