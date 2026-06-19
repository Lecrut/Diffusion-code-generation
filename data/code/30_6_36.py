class StringSwapper:
    SWAP_INCREMENT = 1

    @staticmethod
    def swap_adjacent(s):
        char_list = list(s)
        for i in range(len(char_list) - StringSwapper.SWAP_INCREMENT):
            char_list[i], char_list[i + StringSwapper.SWAP_INCREMENT] = (
                char_list[i + StringSwapper.SWAP_INCREMENT],
                char_list[i]
            )
        return ''.join(char_list)

if __name__ == '__main__':
    test_string = "abcdef"
    swapper = StringSwapper()
    result = swapper.swap_adjacent(test_string)
    print(result)