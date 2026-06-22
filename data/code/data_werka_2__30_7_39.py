class StringReverser:
    @staticmethod
    def swap_characters(s):
        s_list = list(s)
        n = len(s_list)
        for i in range(n // 2):
            s_list[i], s_list[n - i - 1] = s_list[n - i - 1], s_list[i]
        return ''.join(s_list)

if __name__ == '__main__':
    sample_string = "abcdefgh"
    reversed_string = StringReverser.swap_characters(sample_string)
    print(reversed_string)