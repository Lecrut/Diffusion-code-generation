def median_index_value(lst):
    if not lst:
        return None
    
    n = len(lst)
    sorted_list = [0] * n
    for i in range(n):
        sorted_list[i] = lst[i]
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    
    if n % 2 == 1:
        mid = n // 2
        result = sorted_list[mid]
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        result = (sorted_list[mid1] + sorted_list[mid2]) / 2.0
    
    return result

if __name__ == '__main__':
    sample_list = [12, 4, 5, 3, 7, 1, 9]
    value = median_index_value(sample_list)
    print(value)