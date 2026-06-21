def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    result = get_penultimate([1, 2, 3, 4])
    print(result)
    result_empty = get_penultimate([1])
    print(result_empty)