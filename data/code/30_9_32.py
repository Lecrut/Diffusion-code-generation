class CustomString:

    def __init__(self, string):
        self.string = string

    def swap_adjacent_pairs(self):
        char_list = list(self.string)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    custom_string = CustomString(sample_string)
    result = custom_string.swap_adjacent_pairs()
    print(result)