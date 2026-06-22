def reverse_sentence_in_place(sentence):
    if not isinstance(sentence, str):
        raise ValueError('Input must be a string')
    char_list = list(sentence)
    left, right = (0, len(char_list) - 1)
    while left < right:
        char_list[left], char_list[right] = (char_list[right], char_list[left])
        left += 1
        right -= 1
    return ''.join(char_list)
if __name__ == '__main__':
    sample_sentence = 'Hello, World!'
    try:
        reversed_sentence = reverse_sentence_in_place(sample_sentence)
        print(reversed_sentence)
    except ValueError as e:
        print(e)