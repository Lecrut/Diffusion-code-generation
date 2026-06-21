ALLOWED_ELEMENTS = frozenset([2, 4, 6, 8, 10])

def is_element_in_set(element):
    return element in ALLOWED_ELEMENTS

if __name__ == '__main__':
    test_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {element: is_element_in_set(element) for element in test_elements}
    print(results)