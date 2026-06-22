def extend_with_last_element(lst, n):
    if not lst or n < 0:
        raise ValueError("List cannot be empty and number of copies must be non-negative")
    lst.extend([lst[-1]] * n)

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 3
    extend_with_last_element(sample_list, num_copies)
    print(sample_list)