def reverse_string_in_place(char_list):
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    char_list = list(word)
    reverse_string_in_place(char_list)
    return ''.join(char_list)

class StringReverser:
    def __init__(self, word):
        self.word = word
    def get_reversed_word(self):
        char_list = list(self.word)
        reverse_string_in_place(char_list)
        return ''.join(char_list)

if __name__ == '__main__':
    sample_word1 = 'hello'
    print(reverse_word(sample_word1))

    sample_word2 = 'world'
    reverser = StringReverser(sample_word2)
    print(reverser.get_reversed_word())