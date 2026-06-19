class StringManipulator:

    def swap_all_pairs(self, text):
        char_list = list(text)
        length = len(char_list)
        for i in range(0, length - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)
if __name__ == '__main__':
    sample_text = 'abcdefg'
    manipulator = StringManipulator()
    swapped_text = manipulator.swap_all_pairs(sample_text)
    print(swapped_text)