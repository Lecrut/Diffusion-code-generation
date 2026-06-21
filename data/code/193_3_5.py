def sum_list(lst):
    return sum(lst) if lst else 0

if __name__ == '__main__':
    print(sum_list([10, 20, 30, 40]))
    print(sum_list([]))