import math

def find_median(data):
    if not data:
        return None
    
    n = len(data)
    sorted_data = sorted(data)
    
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    sample_list = [7, 1, 3, 4, 6, 5, 2]
    result = find_median(sample_list)
    print(result)
    
    sample_list_even = [7, 1, 3, 4, 6, 5, 2, 8]
    result_even = find_median(sample_list_even)
    print(result_even)