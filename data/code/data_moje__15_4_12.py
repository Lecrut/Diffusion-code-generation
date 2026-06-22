def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    result1 = get_penultimate([1, 2, 3])
    print(result1)
    result2 = get_penultimate([1])
    print(result2)
    result3 = get_penultimate([])
    print(result3)
    result4 = get_penultimate([42, 99, 13, 5])
    print(result4)