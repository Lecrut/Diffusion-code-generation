def find_middle_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [2.5, 3.6, 4.7, 5.8, 6.9]
    try:
        print(find_middle_element(sample_list))
    except (TypeError, ValueError) as e:
        print(e)