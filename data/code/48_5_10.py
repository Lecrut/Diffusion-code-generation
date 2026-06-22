def find_largest_data_point(*collections):
    if not collections:
        return None
    
    largest = None
    
    for collection in collections:
        if not collection:
            continue
            
        for item in collection:
            if isinstance(item, (int, float)):
                if largest is None or item > largest:
                    largest = item
    
    return largest

if __name__ == '__main__':
    list_a = [10, 25, 5, 88, 3]
    list_b = [50, 12, 99, 4]
    list_c = [20, 30, 101, 15]
    
    result = find_largest_data_point(list_a, list_b, list_c)
    print(result)