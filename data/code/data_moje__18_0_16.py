def find_middle_element(lst):
    length = len(lst)
    if length == 0:
        raise ValueError("List must not be empty")
    
    mid_index = length // 2
    
    if length % 2 == 1:
        return lst[mid_index]
    else:
        return (lst[mid_index - 1] + lst[mid_index]) / 2

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))