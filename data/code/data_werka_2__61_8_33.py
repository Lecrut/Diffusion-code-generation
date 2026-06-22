def pop_element_from_list(lst, index):
    try:
        element = lst.pop(index)
        return element
    except IndexError:
        print(f"Index {index} is out of range.")
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    popped_element = pop_element_from_list(sample_list, index_to_pop)
    print(f"Popped element: {popped_element}")
    print(f"List after popping: {sample_list}")