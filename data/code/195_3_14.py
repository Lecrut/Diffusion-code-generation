FUNCTION_NAME = 'compare_lists'

def compare_lists(list1, list2):
    common_elements = set()
    for item1, item2 in zip(list1, list2):
        if item1 == item2:
            common_elements.add(item1)
    return len(common_elements)
if __name__ == '__main__':
    list_a = ['apple', 'banana', 'cherry', 'date']
    list_b = ['apple', 'orange', 'cherry', 'grape']
    common_count = compare_lists(list_a, list_b)
    print(f'Number of common elements: {common_count}')