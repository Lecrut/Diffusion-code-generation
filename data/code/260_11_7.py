def find_max_in_sets(*sets):
    return {s: max(s) for s in sets if s}

if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    set2 = {5, 4, 3, 2, 1}
    set3 = {1, 2, 3, 5}
    set4 = {1, 2, 3, 6}
    
    result1 = find_max_in_sets(set1, set2)
    print(f"Max in sets: {result1}")
    
    result2 = find_max_in_sets(set1, set3)
    print(f"Max in sets: {result2}")
    
    result3 = find_max_in_sets(set1, set4)
    print(f"Max in sets: {result3}")