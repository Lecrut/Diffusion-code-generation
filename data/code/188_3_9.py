def reverse_list_comprehension(lst):
    return [item for item in reversed(lst)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list_comprehension(sample_list))