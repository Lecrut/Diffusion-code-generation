class CustomString:

    def __init__(self, value):
        self.value = value

    def swap_adjacent_pairs(self):
        char_list = list(self.value)
        length = len(char_list)
        for i in range(0, length - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_string = CustomString('abcdefg')
    result = sample_string.swap_adjacent_pairs()
    print(result)