def max_difference(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists.")
    if len(list_a) == 0 or len(list_b) == 0:
        raise ValueError("Both lists must contain at least one element.")
    
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    
    return max(max_a - min_b, max_b - min_a)

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    print(max_difference(list_a, list_b))