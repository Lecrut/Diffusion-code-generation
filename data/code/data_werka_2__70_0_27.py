def check_first_and_last(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    def get_first_element(l):
        return l[0]
    
    def get_last_element(l):
        return l[-1]
    
    first = get_first_element(lst)
    last = get_last_element(lst)
    return first, last

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    first, last = check_first_and_last(sample_list)
    print(first, last)