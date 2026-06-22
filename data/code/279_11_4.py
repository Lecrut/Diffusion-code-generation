def print_reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_reverse(sample_list)