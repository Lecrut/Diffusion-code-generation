def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        temp = lst[i]
        lst[i] = lst[length - i - 1]
        lst[length - i - 1] = temp
    return lst

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)