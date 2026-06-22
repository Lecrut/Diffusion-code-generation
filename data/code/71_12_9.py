def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    mid1 = lst[n // 2 - 1]
    mid2 = lst[n // 2]
    return (mid1 + mid2) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 3, 5, 7, 9, 11]
    print(find_middle(odd_list))
    print(find_middle(even_list))