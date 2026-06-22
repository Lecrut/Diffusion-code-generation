class CustomString:

    def __init__(self, s):
        self.s = s

    def swap_adjacent_pairs(self):
        char_list = list(self.s)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_string = CustomString('abcdefg')
    swapped_string = sample_string.swap_adjacent_pairs()
    print(swapped_string)