def get_central_element(arr):
    index = len(arr) // 2
    return arr[index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    
    odd_result = get_central_element(odd_list)
    even_result = get_central_element(even_list)
    
    print(odd_result)
    print(even_result)