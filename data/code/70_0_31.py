def check_first_and_last(lst):
    def is_list_empty(input_list):
        return len(input_list) == 0

    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if is_list_empty(lst):
        raise ValueError("List cannot be empty")
    
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    first, last = check_first_and_last(sample_list)
    print(first, last)