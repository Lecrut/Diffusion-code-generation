def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string')
    char_list = list(word)
    length = len(char_list)
    mid_point = length // 2
    for i in range(mid_point):
        char_list[i], char_list[length - i - 1] = (char_list[length - i - 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_words = {'hello': 'olleh', 'world': 'dlrow', 'example': 'elpmaxe'}
    for word, expected in sample_words.items():
        try:
            result = reverse_word(word)
            print(f'Original: {word}, Reversed: {result}')
            assert result == expected, f'Test failed for input: {word}'
        except ValueError as e:
            print(e)