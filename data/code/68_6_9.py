def max_difference(list_a, list_b):
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    
    return max(max(max_a - min_b, max_b - min_a), abs(min_a - max_b), abs(min_b - max_a))

if __name__ == '__main__':
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]
    result = max_difference(list_a, list_b)
    print(result)