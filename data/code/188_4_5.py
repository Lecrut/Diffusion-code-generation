from functools import reduce

def reverse_with_reduce(lst):
    return reduce(lambda acc, x: [x] + acc, lst, [])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_with_reduce(sample_list)
    print(reversed_list)