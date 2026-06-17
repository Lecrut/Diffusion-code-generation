def calculate_sum(data):
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
    try:
        sum1 = calculate_sum(list1)
        print(f"Sum of {list1}: {sum1}")
        sum2 = calculate_sum(list2)
        print(f"Sum of {list2}: {sum2}")
        calculate_sum(list3)
    except TypeError as e:
        print(f"Error encountered for list3: {e}")
    try:
        sum4 = calculate_sum(list4)
        print(f"Sum of {list4}: {sum4}")
    except TypeError as e:
        print(f"Error encountered for list4: {e}")