class StringManipulator:

    def swap_all_pairs(self, text):
        chars = list(text)
        length = len(chars)
        for i in range(0, length - 1, 2):
            chars[i], chars[i + 1] = (chars[i + 1], chars[i])
        return ''.join(chars)
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_text = 'abcdef'
    result = manipulator.swap_all_pairs(sample_text)
    print(result)