def find_largest_across_collections(*collections):
    if not collections:
        return None
    
    largest_value = None
    
    for collection in collections:
        if not isinstance(collection, (list, tuple, set)):
            continue
        for item in collection:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                if largest_value is None or item > largest_value:
                    largest_value = item
    
    return largest_value

if __name__ == '__main__':
    list_a = [10, 25, 5, 100, 3]
    list_b = [50, 200, 15, 75]
    list_c = [30, 150, 99, 42]
    
    result = find_largest_across_collections(list_a, list_b, list_c)
    print(result)