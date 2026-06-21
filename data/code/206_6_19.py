SMALLEST_ELEMENT_INDEX = 0

def find_smallest_element(lst):
    if not lst:
        raise ValueError("List is empty")
    smallest_index = SMALLEST_ELEMENT_INDEX
    for i, element in enumerate(lst[1:], start=1):
        if element < lst[smallest_index]:
            smallest_index = i
    return lst[smallest_index]

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_smallest_element(sample_list))