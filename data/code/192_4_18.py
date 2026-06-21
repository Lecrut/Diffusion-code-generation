TOLERANCE = 1e-9

def are_close(a, b):
    return abs(a - b) < TOLERANCE

def find_common_elements(list_a, list_b):
    common_elements = []
    for item_a in list_a:
        if any(are_close(item_a, item_b) for item_b in list_b):
            common_elements.append(item_a)
    return common_elements

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)