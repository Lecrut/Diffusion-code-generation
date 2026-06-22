class StringManipulator:
    PAIR_SIZE = 2

    def swap_all_pairs(self, text):
        char_list = list(text)
        length = len(char_list)
        for i in range(0, length - self.PAIR_SIZE + 1, self.PAIR_SIZE):
            self._swap_characters(char_list, i, i + 1)
        return ''.join(char_list)

    @staticmethod
    def _swap_characters(lst, index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_text = 'abcdefg'
    result = manipulator.swap_all_pairs(sample_text)
    print(result)