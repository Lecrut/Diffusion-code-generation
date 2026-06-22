class StringManipulator:
    def swap_all_pairs(self, text):
        if len(text) < 2:
            return text
        char_list = list(text)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        return ''.join(char_list)

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_text = 'abcdefg'
    result = manipulator.swap_all_pairs(sample_text)
    print(result)