import functools

def reverse_with_reduce(lst):
    return functools.reduce(lambda acc, x: [x] + acc, lst, [])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_with_reduce(sample_list)
    print(reversed_list)