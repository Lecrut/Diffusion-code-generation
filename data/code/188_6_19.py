def reverse_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    reversed_items = list(reverse_generator(sample_list))
    print(reversed_items)