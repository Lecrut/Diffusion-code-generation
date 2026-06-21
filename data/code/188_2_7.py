def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reversed_sample = reverse_using_iter(sample_list)
    print(reversed_sample)