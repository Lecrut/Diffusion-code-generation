def get_central_element(arr):
    if not arr:
        return None
    index = len(arr) // 2
    return arr[index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    
    result_odd = get_central_element(odd_list)
    print(result_odd)
    
    result_even = get_central_element(even_list)
    print(result_even)