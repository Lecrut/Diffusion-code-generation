def find_second_element(data):
    if len(data) < 2:
        raise IndexError("List has fewer than two elements")
    def recursive_search(index):
        if index == 1:
            return data[index]
        return recursive_search(index + 1)
    return recursive_search(0)

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15]
    list3 = [7]
    list4 = [99]
    try:
        print(f"Second element of {list1}: {find_second_element(list1)}")
        print(f"Second element of {list2}: {find_second_element(list2)}")
        print(f"Second element of {list3}: {find_second_element(list3)}")
    except IndexError as e:
        print(f"Error for list with fewer than two elements: {e}")