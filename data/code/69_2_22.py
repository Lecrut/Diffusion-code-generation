def reverse_list_in_place(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
    return lst

if __name__ == '__main__':
    sample_list = [6, 7, 8, 9, 10]
    reversed_list = reverse_list_in_place(sample_list)
    print(reversed_list)