def sum_list(lst):
    if not lst:
        return 0
    return sum(lst)

if __name__ == '__main__':
    print(sum_list([10, 20, 30, 40]))
    print(sum_list([]))