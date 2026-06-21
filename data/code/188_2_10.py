def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    reversed_list = reverse_using_iter(sample_list)
    print(reversed_list)