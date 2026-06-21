def sum_list(lst):
    return sum(lst) if lst else 0

if __name__ == '__main__':
    result = sum_list([15, 25, 35])
    print(result)