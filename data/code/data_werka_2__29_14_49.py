def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string')

    def reverse_string(s):
        return ''.join(reversed(s))
    return reverse_string(word)
if __name__ == '__main__':
    sample_values = ['hello', '', 'a', 'Alibaba Cloud']
    for value in sample_values:
        print(reverse_word(value))