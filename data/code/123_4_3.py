def calculate_list_sum(data):
    total = 0
    for item in data:
        if not isinstance(item, int):
            raise TypeError("List must contain only integers.")
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [1, 2, "three", 4]
    list4 = []
    try:
        sum1 = calculate_list_sum(list1)
        print(f"Sum of {list1}: {sum1}")
        sum2 = calculate_list_sum(list2)
        print(f"Sum of {list2}: {sum2}")
        print("Attempting to calculate sum for list3...")
        sum3 = calculate_list_sum(list3)
        print(f"Sum of {list3}: {sum3}")
    except TypeError as e:
        print(f"Error caught for list3: {e}")
    try:
        sum4 = calculate_list_sum(list4)
        print(f"Sum of {list4}: {sum4}")
    except TypeError as e:
        print(f"Error caught for list4: {e}")