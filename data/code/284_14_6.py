def reverse_list(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)