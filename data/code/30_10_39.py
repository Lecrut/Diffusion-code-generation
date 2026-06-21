class StringSwapper:
    def __init__(self, s):
        self.string = s

    def swap_adjacent_characters(self):
        char_list = list(self.string)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        return ''.join(char_list)

if __name__ == '__main__':
    sample_string1 = 'abcdefg'
    swapper1 = StringSwapper(sample_string1)
    print(swapper1.swap_adjacent_characters())

    sample_string2 = 'hello'
    swapper2 = StringSwapper(sample_string2)
    print(swapper2.swap_adjacent_characters())