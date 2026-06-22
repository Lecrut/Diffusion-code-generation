def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    fruits = ["mango", "papaya", "guava", "kiwi"]
    position_to_fetch = 1
    fetched_element = get_element_by_position(fruits, position_to_fetch)
    print("Element at position", position_to_fetch, ":", fetched_element)
    
    invalid_position = 5
    element_from_invalid_position = get_element_by_position(fruits, invalid_position)
    print("Element at position", invalid_position, ":", element_from_invalid_position)