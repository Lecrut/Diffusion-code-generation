def calculate_list_sum(numbers):
    total = 0
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("List contains non-numeric types.")
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Sum of {list1}: {calculate_list_sum(list1)}")
    list2 = [10.5, 20, -5.5]
    print(f"Sum of {list2}: {calculate_list_sum(list2)}")
    list3 = [1, 'a', 3]
    try:
        calculate_list_sum(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")