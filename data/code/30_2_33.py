class StringManipulator:
    PAIR_SIZE = 2

    def swap_all_pairs(self, text):
        char_list = list(text)
        for i in range(0, len(char_list) - self.PAIR_SIZE + 1, self.PAIR_SIZE):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        return ''.join(char_list)

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_text = 'abcdefg'
    swapped_text = manipulator.swap_all_pairs(sample_text)
    print(swapped_text)