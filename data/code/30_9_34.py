class CustomString:

    def __init__(self, input_string):
        self.input_string = input_string

    def swap_adjacent_pairs(self):
        char_list = list(self.input_string)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    custom_str = CustomString(sample_string)
    result = custom_str.swap_adjacent_pairs()
    print(result)