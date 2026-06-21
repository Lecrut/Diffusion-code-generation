def reverse_list(lst):
    lst.reverse()
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('Original list:', sample_list)
    reversed_sample = reverse_list(sample_list)
    print('Reversed list:', reversed_sample)