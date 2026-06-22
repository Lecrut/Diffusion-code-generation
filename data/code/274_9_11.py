UNIQUE_ELEMENTS = set()

def print_unique_elements(elements):
    global UNIQUE_ELEMENTS
    UNIQUE_ELEMENTS.clear()
    for element in elements:
        if element not in UNIQUE_ELEMENTS:
            UNIQUE_ELEMENTS.add(element)
            print(element)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print_unique_elements(sample_list)