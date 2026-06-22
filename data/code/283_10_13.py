def are_elements_unique(lst):
    unique_items = set()
    for item in lst:
        if item in unique_items:
            return False
        unique_items.add(item)
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))