def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    print(get_penultimate([1, 2, 3, 4]))
    print(get_penultimate([1]))
    print(get_penultimate([]))
    print(get_penultimate([10, 20]))