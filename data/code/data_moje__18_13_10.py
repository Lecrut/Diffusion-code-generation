def get_center_element(array):
    if not array:
        return None
    index = len(array) // 2
    return array[index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [5, 15, 25, 35]
    empty_list = []
    
    print(get_center_element(odd_list))
    print(get_center_element(even_list))
    print(get_center_element(empty_list))