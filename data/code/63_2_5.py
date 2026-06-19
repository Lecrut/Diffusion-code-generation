def retrieve_first_element(elements):
    if not elements:
        raise ValueError("The list is empty.")
    return elements[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    print(retrieve_first_element(sample_list))