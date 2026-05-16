import random
def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    print(f"List 1: {list1}")
    result1 = find_first_element_o1(list1)
    print(f"First element of List 1: {result1}")
    list2 = [999, 1, 5, 1000000]
    print(f"List 2: {list2}")
    result2 = find_first_element_o1(list2)
    print(f"First element of List 2: {result2}")
    list3 = [42]
    print(f"List 3: {list3}")
    result3 = find_first_element_o1(list3)
    print(f"First element of List 3: {result3}")
    list4 = []
    print(f"List 4: {list4}")
    try:
        result4 = find_first_element_o1(list4)
        print(f"First element of List 4: {result4}")
    except IndexError as e:
        print(f"Error for List 4: {e}")