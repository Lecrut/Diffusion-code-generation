import random
def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [99, 1, 5, 1000]
    list3 = [42]
    list4 = []
    print(f"List 1: {list1}")
    print(f"First element of List 1: {find_first_element_o1(list1)}")
    print(f"\nList 2: {list2}")
    print(f"First element of List 2: {find_first_element_o1(list2)}")
    print(f"\nList 3: {list3}")
    print(f"First element of List 3: {find_first_element_o1(list3)}")
    print(f"\nList 4: {list4}")
    try:
        find_first_element_o1(list4)
    except IndexError as e:
        print(f"Error for List 4: {e}")