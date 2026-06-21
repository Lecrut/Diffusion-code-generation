def calculate_list_sum(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    total = 0
    for item in iterable:
        if not isinstance(item, (int, float)):
            raise TypeError("All elements of the iterable must be numbers")
        
        total += item
    
    return total

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    list3 = [-1, 5, -10, 2]
    empty_list = []
    
    try:
        print(f"Sum of {list1}: {calculate_list_sum(list1)}")
        print(f"Sum of {list2}: {calculate_list_sum(list2)}")
        print(f"Sum of {list3}: {calculate_list_sum(list3)}")
        print(f"Sum of {empty_list}: {calculate_list_sum(empty_list)}")
    except (ValueError, TypeError) as e:
        print(e)