def get_middle_index(seq):
    n = len(seq)
    return (n - 1) // 2 if isinstance(seq, list) else int(n / 2)
if __name__ == '__main__':
    data_list = [0, 1, 2]
    print(get_middle_index(data_list))