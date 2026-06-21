def get_penultimate(lst):
    if lst is None:
        return None
    length = len(lst)
    if length < 2:
        return None
    return lst[length - 2]

if __name__ == '__main__':
    print(get_penultimate([1, 2, 3, 4]))
    print(get_penultimate([10]))
    print(get_penultimate([]))
    print(get_penultimate([5, 10]))