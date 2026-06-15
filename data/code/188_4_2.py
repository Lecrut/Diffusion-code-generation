def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reverse_list(sample_list)
    print(f"Reversed list: {sample_list}")
    sample_list_2 = [10, 20, 30, 40]
    print(f"Original list: {sample_list_2}")
    reverse_list(sample_list_2)
    print(f"Reversed list: {sample_list_2}")
    sample_list_3 = [1, 2, 3, 4]
    print(f"Original list: {sample_list_3}")
    reverse_list(sample_list_3)
    print(f"Reversed list: {sample_list_3}")
    sample_list_4 = [5]
    print(f"Original list: {sample_list_4}")
    reverse_list(sample_list_4)
    print(f"Reversed list: {sample_list_4}")