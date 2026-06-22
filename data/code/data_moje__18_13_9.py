def get_central_element(arr):
    n = len(arr)
    index = (n - 1) // 2
    return arr[index]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4]
    
    result_odd = get_central_element(sample_odd)
    result_even = get_central_element(sample_even)
    
    print(result_odd)
    print(result_even)