def get_middle_element(items):
    if not items:
        raise ValueError("List cannot be empty")
    count = len(items)
    offset = count // 2
    if count % 2 == 0:
        offset = offset - 1
    result = items[offset]
    return result

if __name__ == '__main__':
    sample_odd = [7, 8, 9, 10, 11]
    sample_even = [1, 2, 3, 4]
    sample_single = [42]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))
    print(get_middle_element(sample_single))