def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_odd_numbers = [7, 14, 21, 28, 35]
    sample_even_numbers = [10, 20, 30, 40, 50, 60]
    
    middle_odd = find_middle_element(sample_odd_numbers)
    middle_even = find_middle_element(sample_even_numbers)
    
    print(f"The middle element of the odd list is: {middle_odd}")
    print(f"The middle element of the even list is: {middle_even}")