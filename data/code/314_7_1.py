def calculate_list_sum(data):
    total = 0
    for item in data:
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    result1 = calculate_list_sum(list1)
    print(f"Sum of {list1}: {result1}")
    list2 = [10, -5, 20, 0, 3]
    result2 = calculate_list_sum(list2)
    print(f"Sum of {list2}: {result2}")
    list3 = []
    result3 = calculate_list_sum(list3)
    print(f"Sum of {list3}: {result3}")
    list4 = [1000]
    result4 = calculate_list_sum(list4)
    print(f"Sum of {list4}: {result4}")