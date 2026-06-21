class StringSwapper:
    @staticmethod
    def swap_even_odd_indices(s: str) -> str:
        char_list = list(s)
        for i in range(0, len(char_list) - 1, 2):
            char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
        return ''.join(char_list)

if __name__ == '__main__':
    sample_input = 'abcdefg'
    result = StringSwapper.swap_even_odd_indices(sample_input)
    print(result)