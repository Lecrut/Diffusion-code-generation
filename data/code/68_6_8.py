def max_absolute_difference(list_a, list_b):
    if not list_a or not list_b:
        return 0
    
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    
    return max(max_a - min_b, max_b - min_a)

if __name__ == '__main__':
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]
    result = max_absolute_difference(list_a, list_b)
    print(result)