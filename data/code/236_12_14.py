def extend_list_with_last_element(lst, n):
    lst.extend([lst[-1]] * n)

if __name__ == '__main__':
    sample_list = [4, 5, 6]
    num_copies = 2
    extend_list_with_last_element(sample_list, num_copies)
    print(sample_list)