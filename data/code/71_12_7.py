def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    mid_index = length // 2
    if length % 2 == 1:
        return lst[mid_index]
    return (lst[mid_index - 1] + lst[mid_index]) / 2

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    print(find_middle(odd_list))
    print(find_middle(even_list))