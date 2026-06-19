def find_second_element(data):
    if len(data) < 2:
        raise IndexError("List has fewer than two elements")
    return _find_second_element_recursive(data, 0)

def _find_second_element_recursive(data, index):
    if index == 1:
        return data[index]
    return _find_second_element_recursive(data, index + 1)

if __name__ == '__main__':
    sample_lists = {
        "list1": [10, 20, 30, 40],
        "list2": [5, 15],
        "list3": [7],
        "list4": [99],
        "list5": [1, 2, 3]
    }
    
    for name, lst in sample_lists.items():
        try:
            print(f"Second element of {name}: {find_second_element(lst)}")
        except IndexError as e:
            print(f"Error for {name}: {e}")