def sum_list_elements(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("List contains non-numeric elements")
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20, -5.5]
    list3 = [1, 'a', 3]
    list4 = []
    print(f"Sum of {list1}: {sum_list_elements(list1)}")
    print(f"Sum of {list2}: {sum_list_elements(list2)}")
    try:
        sum_list_elements(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")
    print(f"Sum of {list4}: {sum_list_elements(list4)}")