def find_median_binary_search(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(find_median_binary_search(sample_list))