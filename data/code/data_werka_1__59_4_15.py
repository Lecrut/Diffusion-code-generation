def find_middle_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    def calculate_middle_index(length):
        return length // 2
    
    middle_index = calculate_middle_index(len(lst))
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [2.1, 3.4, 5.6, 7.8, 9.0]
    print(find_middle_element(sample_list))