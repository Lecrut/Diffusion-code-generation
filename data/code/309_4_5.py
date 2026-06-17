def calculate_list_sum(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("List contains non-numeric elements.")
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20, -5.5]
    list3 = [1, 'a', 3]
    list4 = []
    print(f"Sum of {list1}: {calculate_list_sum(list1)}")
    print(f"Sum of {list2}: {calculate_list_sum(list2)}")
    try:
        calculate_list_sum(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")
    print(f"Sum of {list4}: {calculate_list_sum(list4)}")