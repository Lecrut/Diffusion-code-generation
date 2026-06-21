from functools import reduce

def reverse_with_reduce(lst):
    return reduce(lambda acc, x: [x] + acc, lst, [])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_with_reduce(sample_list))
    sample_list_2 = ['a', 'b', 'c', 'd']
    print(reverse_with_reduce(sample_list_2))
    sample_list_3 = [10, 20, 30]
    print(reverse_with_reduce(sample_list_3))