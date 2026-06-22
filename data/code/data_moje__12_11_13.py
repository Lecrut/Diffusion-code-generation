def get_middle_element(tup):
    if not tup:
        raise ValueError("Empty sequence")
    mid_index = len(tup) // 2
    return tup[mid_index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_middle_element(sample_tuple)
    print(result)