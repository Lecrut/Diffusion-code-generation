def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    mid = n // 2
    if n % 2 == 1:
        return lst[mid]
    else:
        return (lst[mid - 1] + lst[mid]) / 2

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = find_middle(sample_list)
    print(result)