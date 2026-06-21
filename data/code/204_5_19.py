def find_middle_value(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

if __name__ == '__main__':
    sample_list = [7, 3, 5, 9]
    print(find_middle_value(sample_list))