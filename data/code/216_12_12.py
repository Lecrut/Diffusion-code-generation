def find_median(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    median_value = find_median(data)
    print(median_value)