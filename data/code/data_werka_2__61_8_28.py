def pop_element_from_list(lst, index):
    try:
        element = lst.pop(index)
        return element
    except IndexError:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_pop = 2

    try:
        popped_element = pop_element_from_list(sample_list, index_to_pop)
        print(f"Popped element: {popped_element}")
        print(f"Remaining list: {sample_list}")
    except ValueError as e:
        print(e)