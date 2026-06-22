class StringReverser:

    @staticmethod
    def reverse_sentence(sentence):
        char_list = list(sentence)
        left, right = (0, len(char_list) - 1)
        while left < right:
            char_list[left], char_list[right] = (char_list[right], char_list[left])
            left += 1
            right -= 1
        return ''.join(char_list)
if __name__ == '__main__':
    sample_sentence = 'Hello, World!'
    reversed_sentence = StringReverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)