def reverse_recursive(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        return [lst[-1]] + reverse_recursive(lst[:-1])
if __name__ == '__main__':
    print(reverse_recursive([1, 2, 3, 4, 5]))
    print(reverse_recursive(['a', 'b', 'c']))
    print(reverse_recursive([]))
    print(reverse_recursive([7]))