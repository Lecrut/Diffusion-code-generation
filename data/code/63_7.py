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
    print(f"List 1: {list1}, First element: {find_first_element_o1(list1)}")
    print(f"List 2: {list2}, First element: {find_first_element_o1(list2)}")
    print(f"List 3: {list3}, First element: {find_first_element_o1(list3)}")
    try:
        find_first_element_o1(list4)
    except IndexError as e:
        print(f"List 4: {list4}, Error: {e}")