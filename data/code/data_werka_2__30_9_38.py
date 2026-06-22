class CustomString:

    def __init__(self, value):
        self.value = value

    def swap_adjacent_pairs(self):
        if not isinstance(self.value, str):
            raise ValueError('Input must be a string')
        char_list = list(self.value)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_string = CustomString('abcdefg')
    swapped_string = sample_string.swap_adjacent_pairs()
    print(swapped_string)