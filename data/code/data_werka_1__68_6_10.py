def max_difference(list_a, list_b):
    if not list_a or not list_b:
        return 0
    
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    
    diff1 = abs(max_a - min_b)
    diff2 = abs(max_b - min_a)
    
    return max(diff1, diff2)

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 8, 10]
    print(max_difference(list_a, list_b))