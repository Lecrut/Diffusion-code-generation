def find_middle_item(numbers):
    length = len(numbers)
    if length == 0:
        return None
    middle_index = (length - 1) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    
    middle_item_odd = find_middle_item(sample_list_odd)
    middle_item_even = find_middle_item(sample_list_even)
    
    print("Middle item of the odd-length list:", middle_item_odd)
    print("Middle item of the even-length list:", middle_item_even)