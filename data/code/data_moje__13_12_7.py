def get_nth_element(s, n):
    length = len(s)
    if length == 0:
        return None
    if n < 0:
        adjusted_index = length + n
        if adjusted_index < 0:
            return None
        return s[adjusted_index]
    if n >= length:
        return None
    return s[n]

if __name__ == '__main__':
    sample_string = 'python'
    index = 2
    print(get_nth_element(sample_string, index))
    negative_index = -1
    print(get_nth_element(sample_string, negative_index))
    out_of_bounds_index = 10
    print(get_nth_element(sample_string, out_of_bounds_index))
    empty_string = ''
    print(get_nth_element(empty_string, 0))