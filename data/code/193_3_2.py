def sum_list(lst):
    return sum(lst) if lst else 0

if __name__ == '__main__':
    print(sum_list([1, 2, 3]))
    print(sum_list([]))