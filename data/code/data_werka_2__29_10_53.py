class WordReverser:

    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError('Input must be a string')
        self.word = word

    def reverse(self):
        char_list = list(self.word)
        left, right = (0, len(char_list) - 1)
        while left < right:
            char_list[left], char_list[right] = (char_list[right], char_list[left])
            left += 1
            right -= 1
        return ''.join(char_list)

    def reverse_with_slice(self):
        return self.word[::-1]
if __name__ == '__main__':
    sample_word = 'alibaba'
    reverser = WordReverser(sample_word)
    print(reverser.reverse())
    print(reverser.reverse_with_slice())