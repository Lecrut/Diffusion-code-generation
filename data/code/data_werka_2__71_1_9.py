def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    else:
        return lst[(length // 2) - 1]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    print(find_middle(odd_list))
    print(find_middle(even_list))