def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reversed_sample = reverse_list(sample_list)
    print(reversed_sample)