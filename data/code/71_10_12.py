def get_middle(lst):
    if not hasattr(lst, '__len__'):
        raise ValueError("Input must be a sequence")
    if len(lst) == 0:
        raise ValueError("Sequence must not be empty")
    n = len(lst)
    center = n // 2
    if n % 2 == 1:
        return lst[center]
    left_slice = lst[center - 1:center]
    right_slice = lst[center:center + 1]
    return (left_slice[0] + right_slice[0]) / 2.0

if __name__ == '__main__':
    odd_sample = [10, 20, 30, 40, 50]
    even_sample = [10, 20, 30, 40]
    print(get_middle(odd_sample))
    print(get_middle(even_sample))