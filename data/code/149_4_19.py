def reverse_list_with_comprehension(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]

if __name__ == '__main__':
    sample_list = [6, 7, 8, 9, 10]
    reversed_list = reverse_list_with_comprehension(sample_list)
    print(reversed_list)