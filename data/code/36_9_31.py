def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    char_list = list(s)

    def reverse_segment(start, end):
        while start < end:
            char_list[start], char_list[end] = (char_list[end], char_list[start])
            start += 1
            end -= 1
    reverse_segment(0, len(char_list) - 1)
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'Alibaba Cloud AI'
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)