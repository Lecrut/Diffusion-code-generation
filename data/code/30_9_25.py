class CustomString:

    def __init__(self, value):
        self.value = value

    def swap_adjacent_pairs(self):
        chars = list(self.value)
        for i in range(0, len(chars) - 1, 2):
            chars[i], chars[i + 1] = (chars[i + 1], chars[i])
        return ''.join(chars)
if __name__ == '__main__':
    sample_string = CustomString('abcdefg')
    print(sample_string.swap_adjacent_pairs())