def is_numeric(item):
    return isinstance(item, (int, float))

def validate_list(numbers):
    if not all(is_numeric(item) for item in numbers):
        raise TypeError("List contains non-numeric types.")

def calculate_sum(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20, 30.5]
    list3 = [1, 'a', 3]
    list4 = [1, 2, None, 4]
    
    validate_list(list1)
    print(f"Sum of {list1}: {calculate_sum(list1)}")
    
    validate_list(list2)
    print(f"Sum of {list2}: {calculate_sum(list2)}")
    
    try:
        validate_list(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")
    
    try:
        validate_list(list4)
    except TypeError as e:
        print(f"Error for {list4}: {e}")