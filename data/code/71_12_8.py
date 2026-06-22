def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    mid_index = n // 2
    if n % 2 == 1:
        return lst[mid_index]
    else:
        return (lst[mid_index - 1] + lst[mid_index]) / 2

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    print(find_middle(odd_list))
    print(find_middle(even_list))