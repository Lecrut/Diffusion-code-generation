class WordReverser:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        self.word = word

    def _reverse_list(self, char_list):
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1

    def reverse(self):
        char_list = list(self.word)
        self._reverse_list(char_list)
        return ''.join(char_list)

if __name__ == '__main__':
    sample_word_1 = 'hello'
    sample_word_2 = 'world'
    
    reverser_1 = WordReverser(sample_word_1)
    reverser_2 = WordReverser(sample_word_2)
    
    print(reverser_1.reverse())
    print(reverser_2.reverse())