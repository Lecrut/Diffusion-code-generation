def reverse_list(lst):
    n = len(lst)
    left = 0
    right = n - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
    sample_list_2 = [10, 20, 30, 40]
    reversed_list_2 = reverse_list(sample_list_2)
    print(reversed_list_2)
    sample_list_3 = [1, 2, 2, 3, 1]
    reversed_list_3 = reverse_list(sample_list_3)
    print(reversed_list_3)