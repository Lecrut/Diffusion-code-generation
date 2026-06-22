def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    mid_index = (n - 1) // 2
    if n % 2 == 1:
        return lst[mid_index]
    else:
        return (lst[mid_index] + lst[mid_index + 1]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 3, 5, 7]
    print(find_middle(odd_list))
    print(find_middle(even_list))