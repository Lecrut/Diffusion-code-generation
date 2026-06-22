def extend_list_with_last_element(lst, n):
    lst.extend([lst[-1]] * n)
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    extend_list_with_last_element(sample_list, 3)
    print(sample_list)