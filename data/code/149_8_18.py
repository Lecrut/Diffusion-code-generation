def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10]
    result = reverse_list(sample_list)
    print(result)