def contains_element(lst, target):
    return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item1 = 3
    item2 = 6
    print(f"Does the list contain {item1}? {contains_element(sample_list, item1)}")
    print(f"Does the list contain {item2}? {contains_element(sample_list, item2)}")