def sum_list_elements(numbers):
    if not all(isinstance(item, (int, float)) for item in numbers):
        raise ValueError("List contains non-numeric types.")
    return sum(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20, 30.5]
    list3 = [1, 'a', 3]
    list4 = [1, 2, None, 4]

    print(f"Sum of {list1}: {sum_list_elements(list1)}")
    print(f"Sum of {list2}: {sum_list_elements(list2)}")
    try:
        sum_list_elements(list3)
    except ValueError as e:
        print(f"Error for {list3}: {e}")
    try:
        sum_list_elements(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")