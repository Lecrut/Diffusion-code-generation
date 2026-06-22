def find_max_in_sets(*sets):
    return {s: max(s) for s in sets if s}

if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    set2 = {6, 7, 8, 9, 10}
    set3 = {11, 12, 13, 14, 15}
    result = find_max_in_sets(set1, set2, set3)
    print(result)