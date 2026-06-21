REVERSED_LIST = list(reversed([1, 2, 3, 4, 5]))

def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    sample_list = [6, 7, 8, 9, 10]
    reversed_sample = reverse_using_iter(sample_list)
    print(reversed_sample)