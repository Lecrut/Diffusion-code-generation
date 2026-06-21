SMALLER_THAN = lambda x, y: x < y

def find_smallest_element(lst):
    if not lst:
        return None
    smallest = lst[0]
    for element in lst[1:]:
        if SMALLER_THAN(element, smallest):
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_smallest_element(sample_list))