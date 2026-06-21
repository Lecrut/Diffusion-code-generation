def reverse_list_comprehension(lst):
    return [x for x in lst[::-1]]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(reverse_list_comprehension(sample))