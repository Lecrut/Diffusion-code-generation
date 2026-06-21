def int_list_to_bin_list(int_list):
    return [format(n, 'b') for n in int_list]

if __name__ == '__main__':
    sample_ints = [0, 5, 10, 255, 1024]
    result = int_list_to_bin_list(sample_ints)
    print(result)