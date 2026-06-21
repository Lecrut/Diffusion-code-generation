def get_middle_index(n):
    return n // 2

def middle_element(iterable):
    if not iterable:
        raise ValueError("Empty list")
    
    sorted_iterable = sorted(iterable)
    length = len(sorted_iterable)
    mid_index = get_middle_index(length)
    
    if length % 2 == 1:
        return sorted_iterable[mid_index]
    else:
        return (sorted_iterable[mid_index - 1] + sorted_iterable[mid_index]) / 2

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    print(list_a)
    print(middle_element(list_a))
    
    list_b = [10, 20, 30, 40]
    print(list_b)
    print(middle_element(list_b))
    
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(sample_list)
    print(middle_element(sample_list))