def check_first_last(sequence):
    if not sequence:
        return (None, None)
    return (sequence[0], sequence[-1])
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8, 9)
    sample_string = 'hello'
    print(check_first_last(sample_list))
    print(check_first_last(sample_tuple))
    print(check_first_last(sample_string))