def get_third_element(sequence):
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))