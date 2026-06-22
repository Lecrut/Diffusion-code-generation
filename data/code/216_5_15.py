def get_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    return data[n // 2]

if __name__ == '__main__':
    sample_list_even = [1, 2, 3, 4, 5, 6]
    print("Middle value for even length list:", get_middle_value(sample_list_even))
    
    sample_list_odd = [10, 20, 30, 40, 50, 60, 70]
    print("\nMiddle value for odd length list:", get_middle_value(sample_list_odd))
    
    empty_list = []
    print("\nMiddle value for empty list:", get_middle_value(empty_list))