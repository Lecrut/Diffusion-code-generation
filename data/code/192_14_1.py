def find_common_elements(list1, list2):
    set1 = {item.lower() for item in list1}
    set2 = {item.lower() for item in list2}
    common = set1.intersection(set2)
    return sorted([item.capitalize() for item in common])
if __name__ == '__main__':
    list_a = ["Apple", "Banana", "Cherry", "Date"]
    list_b = ["apple", "Fig", "Banana", "Grape"]
    common_items = find_common_elements(list_a, list_b)
    print(common_items)