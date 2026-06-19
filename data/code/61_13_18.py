def get_element(sequence, index):
    return sequence[index]
if __name__ == '__main__':
    sample_tuple = (100, 200, 300, 400, 500)
    sample_list = ['x', 'y', 'z', 'w', 'v']
    print(get_element(sample_tuple, 1))
    print(get_element(sample_list, 3))