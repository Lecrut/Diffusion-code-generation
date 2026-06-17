def print_list_elements(data):
    if data:
        print(*data)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = []
    list3 = ["a", "b", "c"]
    print("List 1:")
    print_list_elements(list1)
    print("\nList 2 (Empty):")
    print_list_elements(list2)
    print("\nList 3:")
    print_list_elements(list3)