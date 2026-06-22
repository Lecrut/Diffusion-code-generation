def find_middle_element(lst):
    if not isinstance(lst, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(lst) == 0:
        raise ValueError("Input sequence must not be empty")
    n = len(lst)
    index = (n - 1) // 2
    return lst[index]

if __name__ == '__main__':
    odd_sample = [5, 10, 15, 20, 25]
    even_sample = [5, 10, 15, 20]
    print(find_middle_element(odd_sample))
    print(find_middle_element(even_sample))