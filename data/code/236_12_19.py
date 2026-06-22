def extend_with_last(lst, n):
    lst.extend([lst[-1]] * n)

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 5
    extend_with_last(sample_list, num_copies)
    print(sample_list)