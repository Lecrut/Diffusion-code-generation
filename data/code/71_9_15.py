def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        raise ValueError("The list is empty")
    return lst[(n - 1) // 2]

if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    print(find_middle_element(sample_list_odd))
    
    sample_list_even = [2, 4, 6, 8, 10, 12]
    print(find_middle_element(sample_list_even))