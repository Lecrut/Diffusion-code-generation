TOLERANCE = 1e-9

def find_common_elements(list_a, list_b, tolerance=TOLERANCE):
    common_elements = []
    for element in list_a:
        if any(abs(element - other) < tolerance for other in list_b):
            common_elements.append(element)
    return common_elements

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)