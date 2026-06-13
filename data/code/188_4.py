def reverse_list(lst):
    n = len(lst)
    result = [0] * n
    for i in range(n):
        result[i] = lst[n - 1 - i]
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverse_list(sample_list_2)
    print(reversed_list_2)
    sample_list_3 = [10, 20, 30]
    reversed_list_3 = reverse_list(sample_list_3)
    print(reversed_list_3)