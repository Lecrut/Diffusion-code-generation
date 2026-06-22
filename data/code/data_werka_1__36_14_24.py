class StringReverser:

    def __init__(self, sentence):
        self.sentence = sentence

    def reverse_sentence(self):
        char_list = list(self.sentence)
        left, right = (0, len(char_list) - 1)
        while left < right:
            char_list[left], char_list[right] = (char_list[right], char_list[left])
            left += 1
            right -= 1
        self.sentence = ''.join(char_list)

    def get_reversed_sentence(self):
        return self.sentence
if __name__ == '__main__':
    reverser = StringReverser('Hello, World!')
    print(reverser.get_reversed_sentence())
    reverser.reverse_sentence()
    print(reverser.get_reversed_sentence())