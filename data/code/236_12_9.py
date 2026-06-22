def extend_with_last_element(lst, n):
    lst.extend([lst[-1]] * n)

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 3
    extend_with_last_element(sample_list, num_copies)
    print(sample_list)