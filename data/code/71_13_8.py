def find_middle_element(data_list):
    n = len(data_list)
    if n == 0:
        raise IndexError("Cannot find the middle element of an empty list.")
    return data_list[n // 2]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [99]
    sample_list_empty = []
    
    print(f"Middle element of {sample_list_odd}: {find_middle_element(sample_list_odd)}")
    print(f"Middle element of {sample_list_even}: {find_middle_element(sample_list_even)}")
    print(f"Middle element of {sample_list_single}: {find_middle_element(sample_list_single)}")
    try:
        find_middle_element(sample_list_empty)
    except IndexError as e:
        print(f"Error for {sample_list_empty}: {e}")