def compare_min_max(tup1, tup2):
    min_val = min(min(tup1), min(tup2))
    max_val = max(max(tup1), max(tup2))
    return (min_val, max_val)

if __name__ == '__main__':
    result = compare_min_max((3, 5, 7), (2, 8, 9))
    print(result)