def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        temp = lst[i]
        lst[i] = lst[length - i - 1]
        lst[length - i - 1] = temp
    return lst

if __name__ == '__main__':
    sample_list = [13, 24, 35, 46, 57]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)