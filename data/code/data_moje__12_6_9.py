def get_center_element(seq):
    if not seq:
        return None
    length = len(seq)
    center_index = length // 2
    return seq[center_index]

if __name__ == '__main__':
    print(get_center_element([1, 2, 3, 4, 5]))
    print(get_center_element((10, 20, 30)))
    print(get_center_element([42]))
    print(get_center_element([]))