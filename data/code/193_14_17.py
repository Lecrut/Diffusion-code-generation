def sum_list(items):
    if not all(isinstance(item, (int, float)) for item in items):
        raise TypeError("List contains non-numeric types.")
    return sum(items)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Sum of {list1}: {sum_list(list1)}")
    
    list2 = [10.5, 20, 30.5]
    print(f"Sum of {list2}: {sum_list(list2)}")
    
    list3 = [1, 'a', 3]
    try:
        sum_list(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")