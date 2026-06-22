class CustomString:

    def __init__(self, value):
        self.value = value

    def swap_adjacent_pairs(self):
        chars = list(self.value)
        length = len(chars)
        for i in range(0, length - 1, 2):
            chars[i], chars[i + 1] = (chars[i + 1], chars[i])
        self.value = ''.join(chars)
        return self.value
if __name__ == '__main__':
    sample_string = CustomString('abcdefg')
    swapped_string = sample_string.swap_adjacent_pairs()
    print(swapped_string)