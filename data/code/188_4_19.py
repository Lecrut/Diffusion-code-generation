import functools

def reverse_with_reduce(lst):
    return functools.reduce(lambda acc, x: [x] + acc, lst, [])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_with_reduce(sample_list)
    print(reversed_list)
    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverse_with_reduce(sample_list_2)
    print(reversed_list_2)