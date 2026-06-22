def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string')
    char_map = {chr(i): chr(i) for i in range(256)}
    reversed_word = ''
    for char in word:
        reversed_word = char_map[char] + reversed_word
    return reversed_word
if __name__ == '__main__':
    sample_values = ['hello', '', 'a', 'Alibaba Cloud']
    for value in sample_values:
        print(reverse_word(value))